from django.shortcuts import render
from django.http.response import HttpResponse
from django.views import View
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import random

from app.forms import InstaAutoForm

import logging
logger = logging.getLogger(__name__)

# app = Celery('tasks', backend='amqp', broker='amqp://admin:admin@127.0.0.1:5672')

class IndexView(TemplateView):
    template_name = "app/index.html"


class AutoLikeView(FormView):
    template_name = 'app/app.html'
    form_class = InstaAutoForm

    def form_valid(self, form):
        return render(self.request, 'app/app.html', {'form': form})


class AutoLikeConfirmView(FormView):
    template_name = 'app/confirm.html'
    form_class = InstaAutoForm

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

    wait = WebDriverWait(driver=driver, timeout=30)

    def form_valid(self, form):
        # email = form.cleaned_data['insta_email']
        # password = form.cleaned_data['insta_password']
        # num_of_times = form.cleaned_data['insta_num_of_times']
        main(form)
        return render(self.request, 'app/confirm.html', {'form': form})

    """
    以下インスタグラムいいね自動実行の関数
    """
    def main(self, form):
        # 変数
        email = form.cleaned_data['insta_email']
        password = form.cleaned_data['insta_password']
        num_of_times = form.cleaned_data['insta_num_of_times']
        # 他の変数（後でformから入力可能にするかも）
        tags = ['バイク', 'ドラッグスター']

        # ログイン実行
        insta_login(email, password)
        # タグ検索用urlセット（リストで取得）
        tagurllist = tag_search(tags)
        # タグ数に応じてタグ一つに対するいいね回数を選択
        onetaglike_num = 1000 / tagurllist_len
        # タグごとにいいね実行
        for tag in tagurllist:
            driver.get(tag)
            time.sleep(1)
            newest_post()
            # 最新の投稿をいいね
            driver.find_elements_by_class_name('_aagw')[9].click()
            time.sleep(random.randict(3, 6))
            if already_like() == True:
                pass
            else:
                driver.find_element_by_class_name('_aamw').click()
                time.sleep(random.randict(3, 5))
            # 次の投稿をいいね × onetaglike_num
            like_counter = 0
            while like_counter < onetaglike_num:
                if already_like() == True:
                    pass
                else:
                    driver.find_elements_by_xpath('//button[@class="_abl-"]')[2].click()
                    time.sleep(random.randint(3, 6))
                    driver.find_element_by_class_name('_aamw').click()
                    time.sleep(random.randict(3, 5))
                    like_counter += 1
        # ブラウザを閉じる
        driver.quit()



    """
    ログイン
    """
    def insta_login(self, email, password):
        # 変数
        submit_btn_class = '_acan'

        # urlを開く
        driver.get('https://www.instagram.com/')
        # 要素がすべて抽出できるまで待機
        wait.until(EC.presence_of_all_elements_located)
        # メールアドレスとパスワードを入力，及びログイン
        driver.find_element_by_name('username').send_keys(username)
        time.sleep(1)
        driver.find_element_by_name('password').send_keys(password)
        time.sleep(1)
        driver.find_element_by_class_name(submit_btn_class).click()
        wait.until(EC.presence_of_all_elements_located)

        print('インスタグラムにログインしました。')

    """
    タグをurlに変換し配列に格納
    """
    def tag_search(self, tags):
        # 変数
        tagsearchurl = 'https://www.instagram.com/explore/tags/'
        tagurllist = []
        tagurllist_len = 0
        # tagが複数ある場合は分割
        for tag in tags:
            tagurllist_len += 1
            tagurllist.append(tagsearchurl + tag)
        print('タグを配列に格納しました。')
        return tagurllist, tagurllist_len

    """
    既にいいねを押しているかチェック
    """
    def already_like(self):
        likebtnstatus = driver.get_attribute('aria-label')
        if likebtnstatus == '「いいね！」を取り消す':
            return True
        else:
            return False

    """
    最新の投稿まで移動
    """
    def newest_post(self):
        # 変数
        newest_post_class = '_aagw'
        target = driver.find_element_by_class_name(newest_post)[10]
        actions = ActionChains(driver)
        actions.move_to_element(target)
        actions.perform()

        print('最新の投稿まで移動しました。')

        wait.until(EC.presence_of_all_elements_located)
