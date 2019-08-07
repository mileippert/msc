set ANACONDA_PATH=%ANACONDA%;%ANACONDA%\Scripts;%ANACONDA%\Library\usr\bin;%ANACONDA%\Library\bin
set PATH=%ANACONDA_PATH%;%PATH%

%ANACONDA%\Scripts\tensorboard.exe --logdir=.\output\ml_log