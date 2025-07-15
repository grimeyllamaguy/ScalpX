@echo off
echo 📅 Setting up daily 9:29AM launch for ScalpX Bot...

schtasks /create /tn "ScalpX_LiveBot_AutoRun" /tr "\"%cd%\launch_scalpx_bot.bat\"" /sc daily /st 09:29 /rl HIGHEST

echo ✅ Done. Bot will auto-launch daily at 9:29AM.
pause
