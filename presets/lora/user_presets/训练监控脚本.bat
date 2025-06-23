@echo off
echo 正在监控Flux LoRA训练日志...
echo 按Ctrl+C停止监控
echo.
cd /d "D:\workspace\kohya_ss\logs"
echo 监控最新日志文件:
for /f "delims=" %%i in ('dir /b /od *.log 2^>nul') do set newest=%%i
if defined newest (
    echo 日志文件: %newest%
    echo.
    tail -f "%newest%"
) else (
    echo 未找到日志文件，请检查训练是否已开始
    echo 日志目录: %cd%
)
pause 