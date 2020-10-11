@echo off
KodPowrotu.exe /s %*

if %ERRORLEVEL% equ 11 (
	echo Brak parametrow
	goto theEnd
)
if %ERRORLEVEL% equ 12 (
	echo Parametr %* nie jest liczba
	goto theEnd
)
if %ERRORLEVEL% equ 13 (
	echo Niewlasciwa wartosc parametru %*
	goto theEnd
)

echo Przekazano: %ERRORLEVEL%

:theEnd
