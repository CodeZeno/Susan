for %%* in (.) do SET version=%%~nx* v0.08
SET comment=Planning working (30% of the time).
git add -A
git commit -a -m "%version%" -m "" -m "%comment%"
git push
Pause