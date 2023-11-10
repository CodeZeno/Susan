for %%* in (.) do SET version=%%~nx* v0.07
SET comment=Can continue a conversation.
git add -A
git commit -a -m "%version%" -m "" -m "%comment%"
git push
Pause