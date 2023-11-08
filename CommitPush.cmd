for %%* in (.) do SET version=%%~nx* v0.03
SET comment=Now saving agent responses.
git add -A
git commit -a -m "%version%" -m "" -m "%comment%"
git push
Pause