for %%* in (.) do SET version=%%~nx* v0.10
SET comment=Updated WSL2 setup guide.
git add -A
git commit -a -m "%version%" -m "" -m "%comment%"
git push
Pause