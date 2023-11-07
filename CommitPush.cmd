for %%* in (.) do SET version=%%~nx* v0.02
SET comment=Added fetch webpage ability.
git add -A
git commit -a -m "%version%" -m "" -m "%comment%"
git push
Pause