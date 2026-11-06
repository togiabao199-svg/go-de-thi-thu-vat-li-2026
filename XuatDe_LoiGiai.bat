@echo off
setlocal EnableExtensions
rem ================================================================
rem  XUAT DE THI + LOI GIAI TU MOT FILE .TEX (goi ex_test)
rem  Cach dung : keo tha 1 hoac nhieu file .tex vao file .bat nay
rem  Ket qua   : <ten>-DeThi.pdf va <ten>-LoiGiai.pdf nam canh file goc
rem  File goc KHONG bi sua; tuy chon [..] hay \def\CheDo{..} trong file khong quan trong.
rem  Nhan ca file nap ex_test truc tiep lan file dung \input{preamble-eduzy}.
rem ================================================================

rem ---- Trinh bien dich: pdflatex hoac xelatex
set "ENGINE=pdflatex"

rem ---- Cac ban can xuat, dang  tuychon:HauTo  cach nhau boi dau cach
rem      Tuy chon cua ex_test: dethi, loigiai, color, solcolor
rem      Vi du them ban to do dap an:  color:DapAn
set "CHEDO=dethi:DeThi loigiai:LoiGiai"

where %ENGINE% >nul 2>&1 || (
  echo Khong tim thay %ENGINE%. Kiem tra lai MiKTeX/TeX Live.
  goto :Het
)
rem MiKTeX dung --job-name, TeX Live dung -jobname
set "JOBOPT=-jobname"
%ENGINE% --version 2>nul | findstr /i "MiKTeX" >nul && set "JOBOPT=--job-name"

if "%~1"=="" goto :HoiTen
for %%F in (%*) do call :XuLy "%%~fF"
goto :Het

:HoiTen
echo Keo tha file .tex vao cua so nay roi nhan Enter:
set "FILE="
set /p "FILE="
if not defined FILE goto :Het
call :XuLy %FILE%
goto :Het

rem ----------------------------------------------------------------
:XuLy
if /i not "%~x1"==".tex" (
  echo Bo qua "%~nx1" - khong phai file .tex
  exit /b
)
pushd "%~dp1"
set "NAME=%~n1"
echo.
echo ===== %~nx1 =====
findstr /c:"{ex_test}" /c:"preamble-eduzy" "%~nx1" >nul 2>&1 || (
  echo   -^> File nay khong nap goi ex_test hay preamble-eduzy, bo qua.
  popd
  exit /b
)
findstr /c:"Opensolutionfile" "%~nx1" >nul 2>&1 && if not exist "ans\" mkdir "ans"
for %%C in (%CHEDO%) do (
  for /f "tokens=1,2 delims=:" %%a in ("%%C") do call :Build %%a %%b
)
popd
exit /b

rem ----------------------------------------------------------------
:Build
rem %1 = tuy chon ex_test, %2 = hau to ten file xuat
set "OUT=%NAME%-%~2"
echo   Dang xuat %OUT%.pdf ...
if exist "%OUT%.pdf" del "%OUT%.pdf"
rem Ep tuy chon cho ex_test ngay truoc khi goi nay duoc nap
set "EP=\AddToHook{package/ex_test/before}{\expandafter\def\csname opt@ex_test.sty\endcsname{%~1}\expandafter\def\csname @raw@opt@ex_test.sty\endcsname{%~1}}"
rem Bien dich 2 lan de lastpage, tham chieu... cap nhat dung
%ENGINE% -interaction=nonstopmode %JOBOPT%="%OUT%" "%EP%\input{%NAME%}" >nul 2>&1
%ENGINE% -interaction=nonstopmode %JOBOPT%="%OUT%" "%EP%\input{%NAME%}" >nul 2>&1
if exist "%OUT%.pdf" (
  echo   -^> Xong: %OUT%.pdf
  for %%X in ("%OUT%.*") do if /i not "%%~xX"==".pdf" del "%%X"
) else (
  echo   -^> LOI khi bien dich, xem file %OUT%.log
)
exit /b

rem ----------------------------------------------------------------
:Het
echo.
pause
