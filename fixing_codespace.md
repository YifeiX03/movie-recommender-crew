ok i'm going to write down how to fix the error in codespaces\
where when you try to start a crew it just won't

following the instructions here\
https://docs.crewai.com/installation\
up until like here
```
crewai create crew <your_project_name>
```
this doesn't work you get the error:\
RuntimeError: Your system has an unsupported version of sqlite3. Chroma requires sqlite3 >= 3.35.0.\
which sucks, the docs don't help either

ok I'm going to try changing the image for the codespace\
to do this, in vscode go to the top bar and do 
```
>add dev
```
and go for Codespaces: Add Dev Container Configuration Files.\
then go for python3.11-bookworm

and then do the openai set up stuff