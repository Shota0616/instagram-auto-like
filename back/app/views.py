from django.shortcuts import render
from django.http.response import HttpResponse
from django.views import View
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time
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

class MainView(View):
    template_name = 'app/confirm.html'
    form_class = InstaAutoForm

    # def form_valid(self, form):
    #     email = form.cleaned_data['insta_email']
    #     password = form.cleaned_data['insta_password']
    #     # num_of_times = form.cleaned_data['insta_num_of_times']
    #     MainView.test(email, password)
    #     return render(self.request, 'app/confirm.html', {'form': form})

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        MainView.main(email, password)
        params = {
            'email': email,
            'password': password,
        }
        return render(self.request, 'app/confirm.html', params)

    @staticmethod
    def conection_chrome():
        # selenium
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        # options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Remote(
            command_executor="http://chrome:4444/wd/hub",
            options=options,
            # desired_capabilities=DesiredCapabilities.CHROME
        )
        return driver
    """
    以下インスタグラムいいね自動実行の関数
    """
    @staticmethod
    def main(email, password):
        # try:
        logger.info(f'{email}:処理開始')
        driver = MainView.conection_chrome()
        wait = WebDriverWait(driver=driver, timeout=30)
        # 変数
        like_btn_class = '_aamw'
        # 他の変数（後でformから入力可能にするかも）
        tags = ['バイク', 'ドラッグスター']

        # ログイン実行
        MainView.insta_login(email, password)
        # タグの数を取得
        tagurllist_len = len(tags)
        # タグ数に応じてタグ一つに対するいいね回数を選択
        onetaglike_num = 1000 / tagurllist_len
        i = 0
        # タグごとにいいね実行
        for tag in tags:
            # タグ検索用
            MainView.tag_search(driver, tag, email)
            time.sleep(random.randint(2, 5))
            i = i + 1
            logger.info(f'{email}:{i}個目のタグのいいね処理を開始します')
            # 新しいタブでurlを開く
            # driver.execute_script(f"window.open('{tag}');")
            driver.get(tag)
            wait.until(EC.presence_of_all_elements_located)
            time.sleep(random.randint(5, 7))
            # 最新の投稿まで移動
            MainView.newest_post(driver, wait, email)
            # 最新の投稿をいいね
            driver.find_elements(By.CLASS_NAME,'_aagw')[9].click()
            time.sleep(random.randint(2, 5))
            if MainView.already_like(driver) == True:
                pass
            else:
                driver.find_element(By.CLASS_NAME,like_btn_class).click()
                time.sleep(random.randint(3, 5))
            # 次の投稿をいいね × onetaglike_num
            like_counter = 0
            while like_counter < onetaglike_num:
                if MainView.already_like(driver) == True:
                    pass
                else:
                    driver.find_elements(By.XPATH,'//button[@class="_abl-"]')[1].click()
                    time.sleep(random.randint(3, 6))
                    driver.find_element(By.CLASS_NAME,like_btn_class).click()
                    time.sleep(random.randint(3, 5))
                    like_counter += 1
        # ブラウザを閉じる
        driver.quit()

        # 例外処理（現状すべての例外をキャッチ）
        # except:
        #     # ブラウザを閉じる
        #     driver.quit()
        #     logger.error('何かしらのエラーが発生しました')



    """
    ログイン
    """
    @staticmethod
    def insta_login(email, password):

        driver = MainView.conection_chrome()
        wait = WebDriverWait(driver, timeout=30)
        # 変数
        submit_btn_class = '_aj1-'

        # urlを開く
        driver.get('https://www.instagram.com/')
        # 要素がすべて抽出できるまで待機
        wait.until(EC.presence_of_all_elements_located)
        # メールアドレスとパスワードを入力，及びログイン
        time.sleep(random.randint(3, 5))
        driver.find_element(By.NAME,'username').send_keys(email)
        time.sleep(random.randint(2, 5))
        driver.find_element(By.NAME,'password').send_keys(password)
        time.sleep(random.randint(2, 5))
        driver.find_elements(By.CLASS_NAME, submit_btn_class)[1].click()
        wait.until(EC.presence_of_all_elements_located)

        logger.info(f'{email}:ログインしました')

    # """
    # タグをurlに変換し配列に格納
    # """
    # @staticmethod
    # def tag_search(tags, email):
    #     # 変数
    #     tagsearchurl = 'https://www.instagram.com/explore/tags/'
    #     tagurllist = []
    #     # tagが複数ある場合は分割
    #     for tag in tags:
    #         tagurllist.append(tagsearchurl + tag)
    #     logger.info(f'{email}:タグを配列に格納しました')
    #     return tagurllist

    @staticmethod
    def tag_search(driver, tag, email):
        # 変数
        search_btn_class = 'svg[aria-label="検索"]'
        search_field_class = 'input[aria-label="検索語句"]'
        time.sleep(random.randint(3, 6))
        driver.find_element(By.CSS_SELECTOR,search_btn_class).click()
        time.sleep(random.randint(3, 6))
        driver.find_element(By.CSS_SELECTOR,search_field_class).send_keys('#' + tag)
        time.sleep(random.randint(3, 6))
        action = webdriver.ActionChains(driver)
        action.send_keys(Keys.ENTER).perform()
        logger.info(f'{email}:タグ検索OK')

    """
    既にいいねを押しているかチェック
    """
    @staticmethod
    def already_like(driver):
        # 変数
        like_btn_class = 'svg[aria-label="「いいね！」を取り消す"]'
        if len(driver.find_element(By.CSS_SELECTOR,like_btn_class)) > 0:
            return True
        else:
            return False

    """
    最新の投稿まで移動
    """
    @staticmethod
    def newest_post(driver, wait, email):
        wait = WebDriverWait(driver=driver, timeout=30)
        time.sleep(random.randint(4, 6))
        # 変数
        newest_post_class = '_aanc'
        # newest_post_class = '//*[@id="mount_0_0_ia"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/h2'
        # newest_post_class = 'div[class="_ac7v _aang"]'
        target = driver.find_element(By.CSS_SELECTOR,newest_post_class)
        #target = driver.find_element(By.XPATH,newest_post_class)
        actions = ActionChains(driver)
        actions.move_to_element(target)
        actions.perform()
        wait.until(EC.presence_of_all_elements_located)
        logger.info(f'{email}:最新の投稿まで移動しました')
