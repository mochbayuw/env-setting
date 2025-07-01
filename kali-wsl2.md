# Penetration Testing Environment Setting: WSL-2 KALI-LINUX

Instalation guide for Kali Linux in Windows Subsystem for Linux (WSL2) **drive eksternal (E:)**

**System Requirements:**

| **Component** | **Minimum** | **Recommended** |
| --- | --- | --- |
| **Operating System** | Windows 11 Home/Pro (64-bit) | Windows 11 Home/Pro (64-bit) |
| **WSL Version** | WSL2 (with Virtual Machine Platform enabled) | WSL2 (with Virtual Machine Platform enabled) |
| **Processor (CPU)** | 4-core (Intel i5 / Ryzen 3 or equivalent) with virtualization (VT-x/AMD-V) | 6-core or higher |
| **RAM** | 8 GB | 16 GB |
| **Storage** | 40 GB SSD free (20 GB for Kali + 20 GB for workspace) | SSD with 256 GB+ |
| **GPU (optional)** | Integrated GPU | Discrete GPU for smoother GUI (Xfce via KeX) |
| **BIOS Setting** | Virtualization (VT-x/AMD-V) enabled | Virtualization (VT-x/AMD-V) enabled |
| **Internet** | Stable connection for downloads & updates | Stable connection for downloads & updates |
| **Kali Package** | `kali-tools-top10` | `kali-linux-large` |
| **GUI / Desktop** | KeX (basic window mode) | `kex --win -s` (seamless windowed mode) |

## 💻 Step 1: Install WSL 2

### You must be running Windows 10 version 1903 or higher, with Build 18362 or higher, or any version of Windows 11. To check your version: Press `Win + R`, type `winver`, and hit Enter.

1.  Open PowerShell as Administrator.
2.  Run the following commands: `wsl --install`
3.  Restart your PC to apply the changes.
4.  Open PowerShell and run:`wsl --set-default-version 2`

---

## 📦 Step 2: Install Kali Linux via Microsoft Store

1.  Open Microsoft Store and search for **Kali Linux**.
2.  Click **Install** to download and install it.
3.  Open **Kali Linux** from the Start Menu.
4.  Wait for setup to finish, then create a username and password.

---

## 🧰 Step 2: Export Kali Linux to a `.tar` File

1. Make sure the folder `E:\WSL\Kali` already exists. If it doesn't exist, create it manually.
2. Open **PowerShell** or **Command Prompt**, then run:

```bash
wsl --export kali-linux E:\WSL\Kali\kali-export.tar
```

This will export your Kali Linux instance to a `.tar` backup file.

---

## 💾 Step 3: Import Kali Linux to Drive `E:\`

```powershell
wsl --import KaliE E:\WSL\Kali E:\WSL\Kali\kali-export.tar --version 2
```

* `KaliE` = name of the new WSL instance
* `E:\WSL\Kali` = location for the filesystem
* `--version 2` = use WSL 2

---


## 🔐 Jalankan Kali dari Drive E: Login setting, avoid Root login by Default

```powershell
wsl -d KaliE -u <nama user yang kamu setup>
```

```powershell
nano ~/.bashrc
```

baris paling atas taruh kata "cd"

* * *

## Error Evaluating

- Go to windows terminal, then find setting or press Ctrl+,
- check for error icon, if you find error then fix it

## Kali Tool Batch

- Use `sudo apt update && sudo apt upgrade && sudo apt autoremove && sudo apt clean`
- `sudo apt kali-linux-large -y`
- Atau menggunakan

## Buat shortcut

- Di desktop, klik kanan dan pilih new > Shortcut
- Masukan kode ini

```powershell
C:\Windows\System32\wsl.exe -d KaliE -u <username yg dibuat sebelumnya>
```

- Lanjut di halaman selanjutnya masukan nama: wsl.exe
- Klik kanan di shortcut yang dibuat, ganti icon sesuai selera

* * *

## ✅ Hasil Akhir

- Kali Linux berjalan dari \**drive E:\**
- Tidak auto-login sebagai root
- Siap digunakan untuk testing, pentest, atau development

* * *

## 📌 Note

- Don't forget to turn on **WSL** and **Virtual Machine Platform** from Windows Feature before starting.
- Make sure your Windows using **WSL 2** (Windows 10 2004+ / Windows 11)
- Ketika sudah selesai digunakan, jangan lupa eject external storage dan ketik

```powershell
wsl --shutdown
```

* * *

## 📎 License

Distribusi Kali Linux mengikuti lisensi [Offensive Security](https://www.kali.org/docs/policy/kali-linux-licensing/)

* * *
