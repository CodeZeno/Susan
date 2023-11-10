for %%* in (.) do SET version=%%~nx* v0.06
SET comment=Can run multiple abilities to return to LLM.
git add -A
git commit -a -m "%version%" -m "" -m "%comment%"
git push
Pause