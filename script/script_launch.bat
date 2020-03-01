@echo off
chcp 65001 > NUL
echo Testing Python and VLC environment variables, you'll see a window flash
timeout /t 1 > NUL
cls
echo ? VLC
echo ? Python
echo * ? Pip
echo ** ? "send2trash" Module
echo.
timeout /t 1 > NUL
vlc vlc://quit > NUL
if "%ERRORLEVEL%"=="0" (
	cls
	echo ✓ VLC
	echo ? Python
	echo * ? Pip
	echo ** ? "send2trash" Module
	echo.
	timeout /t 1 > NUL
	python -h > NUL
	if "%ERRORLEVEL%"=="0" (
		cls
		echo ✓ VLC
	    echo ✓ Python
		echo * ? Pip
		echo ** ? "send2trash" Module
		echo.
		timeout /t 1 > NUL
		pip -h > NUL
		if "%ERRORLEVEL%"=="0" (
			cls
			echo ✓ VLC
			echo ✓ Python
			echo * ✓ Pip
			echo ** ? "send2trash" Module
			echo.
			timeout /t 1 > NUL
			pip search send2trash | findstr INSTALLED > NUL
			if "%ERRORLEVEL%"=="0" (
				cls
				color 02
				echo ✓ VLC
				echo ✓ Python
				echo * ✓ Pip
				echo ** ✓ "send2trash" Module
				echo.
				echo Everything seems in order, running script and closing this window in a bit
				start python vid-reviewr.py
				timeout /t 3 > NUL
				exit
			)
			else (
			cls
			color C
			echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
			echo.
			echo ✓ VLC
			echo ✓ Python
			echo * ✓ Pip
			echo ** X "send2trash" Module
			echo.
			echo Something went wrong when testing for the "Send2Trash" module. It's possible you're missing it.
			echo.
			echo Please install it using "pip install send2trash" and run the script again
			echo.
			echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
			echo.
			pause
			exit
		)
		else (
		cls
		color C
		echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		echo.
		echo ✓ VLC
	    echo ✓ Python
		echo * X Pip
		echo ** ? "send2trash" Module
		echo.
		echo Something went wrong when testing for Pip. It's possible you're missing it or it doesn't work from CMD
		echo.
		echo Please resolve this before continuing
		echo.
		echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		echo.
		pause
		exit
		)
	)
	else (
		cls
		color C
		echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		echo.
		echo ✓ VLC
		echo X Python
		echo * ? Pip
		echo ** ? "send2trash" Module
		echo.
		echo Something went wrong when testing for Python, you might be missing the Path since it's not set unless you select it.
		echo.
		echo Please add that Path in Windows "Environment Variables"
		echo.
		echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		echo.
		pause
		exit
	)
) else (
	cls
	color C
	echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	echo.
	echo X VLC
	echo ? Python
	echo * ? Pip
	echo ** ? "send2trash" Module
	echo.
	echo Something went wrong when testing for VLC, you're probably missing the Path since it's never set by default.
	echo.
	echo Please add that Path in Windows "Environment Variables"
	echo.
	echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	echo.
	pause
	exit
)