for %%* in (.) do SET version=%%~nx* v0.04
SET comment=Updating version.
git add -A
git commit -a -m "%version%" -m "" -m "%comment%"
git push
Pause