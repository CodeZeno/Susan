for %%* in (.) do SET version=%%~nx* v0.09
SET comment=Added WSL2 setup guide.
git add -A
git commit -a -m "%version%" -m "" -m "%comment%"
git push
Pause