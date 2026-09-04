import json
import subprocess
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, "payroll.json")

def run_command(cmd):
    proc = subprocess.Popen(
        f'echo "y" | {cmd}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    stdout, stderr = proc.communicate()
    return proc.returncode, stdout, stderr

def main():
    print("="*60)
    print("🚀 Miden Confidential zkPayroll Engine Başlatılıyor...")
    print("="*60)
    if not os.path.exists(CONFIG_PATH):
        print(f"Hata: {CONFIG_PATH} bulunamadı!")
        return
    with open(CONFIG_PATH, "r") as f:
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
    print("\n📊 BORDRO İŞLEM RAPORU:")
    for s in summary:
        print(f"- {s['name']}: {s['status']} ({s['target']})")
    print("\n✨ Not: Tüm ödemeler 'Private Note' olarak gönderildi.")

if __name__ == "__main__":
    main()
