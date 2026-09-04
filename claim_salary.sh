#!/bin/bash
echo "🔍 Hesabınıza gelen Private Notlar senkronize ediliyor..."
miden client sync

echo "⚡ Notlar tüketiliyor ve bakiye hesabınıza aktarılıyor..."
echo "y" | miden client consume-notes

echo "🎉 Maaşınız başarıyla hesabınıza aktarıldı!"
miden client account show
