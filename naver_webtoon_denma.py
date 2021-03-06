import os
import requests

image_urls = [
    'http://imgcomic.naver.net/webtoon/119874/1021/20170611184321_d6b0a3d0c1acc8b6af070d3cd7486c5d_IMAG01_1.jpg',
    'http://imgcomic.naver.net/webtoon/119874/1021/20170611184321_d6b0a3d0c1acc8b6af070d3cd7486c5d_IMAG01_2.jpg',
    'http://imgcomic.naver.net/webtoon/119874/1021/20170611184321_d6b0a3d0c1acc8b6af070d3cd7486c5d_IMAG01_3.jpg'
]

for image_url in image_urls:
    headers = {
        'Referer': 'http://comic.naver.com/webtoon/detail.nhn?titleId=119874&no=1021&weekday=tue',
    }
    response = requests.get(image_url, headers=headers)
    image_data = response.content
    filename = os.path.basename(image_url)
    with open(filename, 'wb') as f:
        print('writing to {} ({} bytes)'.format(filename, len(image_data)))
        f.write(image_data)