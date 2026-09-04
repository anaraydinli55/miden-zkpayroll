import json
import subprocess
import os
import time

def run_command(cmd):
    """Miden komutunu çalıştırır ve otomatik 'y' onayı verir."""
    proc = subprocess.Popen(
        f'echo "y" | {cmd}',
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = proc.communicate()
    return proc.returncode, stdout, stderr

def main():
    print("="*60)
    print("🚀 Miden Confidential zkPayroll Engine Başlatılıyor...")
    print("="*60)

    if not os.path.exists("payroll.json"):
        print("Hata: payroll.json bulunamadı!")
        return

    with open("payroll.json", "r") as f:
        employees = json.load(f)

    total = len(employees)
    print(f"📋 Toplam {total} çalışana gizli ödeme yapılacak.\n")

    summary = []

    for idx, emp in enumerate(employees, 1):
        name = emp["employee"]
        target = emp["target_account"]
        amount = emp["amount"]
        token = emp["token_id"]

        print(f"[{idx}/{total}] 🔒 {name} için Private Note oluşturuluyor...")
        print(f"      Adres : {target}")
        print(f"      Miktar: {int(amount)/100000000} SKS")

        # Private note gönderim komutu
        cmd = f"miden client send --target {target} --asset {amount}::{token} --note-type private"
        
        ret, out, err = run_command(cmd)

        if ret == 0:
            print(f"      ✅ Başarılı! ZK Proof doğrulandı ve not ağa mühürlendi.")
            summary.append({"name": name, "status": "SUCCESS", "target": target})
        else:
            print(f"      ❌ Hata oluştu!")
            summary.append({"name": name, "status": "FAILED", "target": target})

        time.sleep(2)
        print("-" * 60)

    # Özet rapor üret
    print("\n📊 BORDRO İŞLEM RAPORU:")
    for s in summary:
        print(f"- {s['name']}: {s['status']} ({s['target']})")
        
    print("\n✨ Not: Tüm ödemeler 'Private Note' olarak gönderildi. Zincir üstü gözetleyiciler miktarları ve alıcıları göremez.")

if __name__ == "__main__":
    main()
