a
    �9
a<  �                   @   s�   d dl Z d dlZed� ed�Ze�d�Zdd�e� Ze�e�Z	e	j
dkrVed� qe	j
dkrqdqed	� ed
d�Ze�d�e�� e��  e �d� dS )�    Nu   激活FlyOS!u   请输入密钥:�-z.http://store.flyosgeek.com/active/key.php?key=�nu<   密钥作废(已被使用)或者格式不正确，请检查!�yu   序列号正确，写入中z5/data/data/com.termux/files/home/.flyos/active/key.fk�wzbash $FLYOS/munu.sh)�osZrequests�print�input�i�split�joinZURL�get�res�text�open�f�write�close�system� r   r   �check.py�<module>   s   





