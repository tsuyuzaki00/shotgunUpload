@ECHO OFF
SETLOCAL
 
SET THISDIR=%~dp0
SET ACTIVATE_VENV=%USERPROFILE%\.virtualenvs\venv_shotgun_scripting\Scripts\activate.bat
SET DEACTIVATE_VENV=%USERPROFILE%\.virtualenvs\venv_shotgun_scripting\Scripts\deactivate.bat
 
CALL %ACTIVATE_VENV%
python %THISDIR%\addVersion.py
CALL %DEACTIVATE_VENV%
 
PAUSE