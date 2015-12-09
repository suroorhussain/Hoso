from setuptools import setup

setup( name ='Hoso',
       version = '0.1',
       description = 'Social media integrator',
       url ='https://github.com/suroorhussain/Hoso',
       author = 'Team Hoso',
       author_email='surusuroor@gmail.com',
       license='MIT',
       packages=['hoso'],
       install_requires=['tweepy', 'facebook-sdk'],
       zip_safe=False
       )
