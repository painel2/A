import subprocess

def baixar_live():
    url = "https://sae11.playlist.ttvnw.net/v1/playlist/CtYGzyCemkvC0qPQyqKR55Jm8YCpkyCK-r8bsylgboYSocOCacfsZrjQZLccMmIXJHI_qJJZ0nLQTaHQnWWanuqgVydsn4WR_JhvgjtfVBbjMmJe0U23mrKvUlebVKTixuNBWe0WNCbcHHWxJJ9d52jSZn5x0QrDYqga-0xyM79bbu-DUQ6vA_Hzq3eClEQpyjdsqM_zW3knSIpguIWTIwz1JHZoiyztCWlJxox8x0E_UBWMoDoo6MmpW_MNoDCIn6Qsu6Oh-iXhGSG12a5XXTz8g6nS9uK3n8SJkX9RPAKfYlD2ucYwzpXbXSG2rfrSUX-dqKBwlYRHPYWqvrk7SXlsAh-LYiRQ8SvXiIACmhcq24JeG07eKr136O0HKiZU3KdTUVZji4_VZT80l1U26guHTrfEppErnq9ZnSER93kTgpxE82eF-v6C3hHk5M7iWcvKgxe9JTlKUHPpfTXczIntmZFuGPnCyd1u7W7fPwmWeqltApDcwSlweMkZajsf3ScQIafwuJvrOX_ljYQSDsRMVn0c6Dh9Bo39omBr-SzQF8qP5sRnBjjD7d9eBM589AoORCLAwmUNp-DmMQ51cUpGDaCdzeWEwZ6S49YLsCbVElCiSxGnZwXXz_ezyyi6QWR0cvmata5Dt6EASGIoFhTDvHKD_16k39sGUkF3JEQwiI_FSs88gh1XOtnkcADuB_IB5Oq78hHuWiB-SdPWzNL8gxOtwTVzdgfml3pKLqS7yZgWEMl_WcusXvLBDzEikb7ZkMUz6VGoPmtFpLlP5stqY1iB0PTQY2D29wvf4ZnjyG2dxvlBZEjnKLHLsfYeLnORqOmUr6D3l2yCgNIfM-pN-xh6Xy43Jx8N2mzOHxjil9QEgCFTfuctNrhfx0kpavX4SlGKDjAKU9zEbd2Dnl5MQBvrc_8wGICJYFPvzUOzyu7bXCDmc9HmZEZtGLFIyomW-dtW9biqhdLrkVhZ8j16JMYgFxB9yCV3Wa1tI2SOqAprXk1lQiItFmycqzWYx2Kpa90G5bfDsJCAGpiXf0RnIak5rZCk2ryiVEZ8-tQA375ECbsO-xS0xE50oNfunRIeVkIvFScAIOXLWZKEe5K72Ss0bFrJgFUE3BsnCYem-F3cTcD_ak8aDJjwLDLnv4-foUboIiABKgl1cy1lYXN0LTIw8ww.m3u8"
    comando = [
        "yt-dlp",
        "-f", "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
        "-o", "live_twitch.mp4",
        url
    ]
    print("Baixando live...")
    subprocess.run(comando, check=True)
    print("Download concluído.")

if __name__ == "__main__":
    baixar_live()
