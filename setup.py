from distutils.core import setup
setup(
  name = 'blissops',
  packages = ['blissops'],
  version = '0.1',
  license='MIT',
  description = 'Simple BytesIO based image manipulation library. No hard work and no good results.',
  author = 'Liam (ir-3) H.',
  author_email = 'i@national.shitposting.agency',
  url = 'https://github.com/blisspy/bliss-ops',
  download_url = 'https://github.com/blisspy/bliss-ops/archive/v_01.tar.gz',
  keywords = ['imageops', 'simple', 'Bad'],
  install_requires=[
          'wand',
          'numpy',
          'scipy',
          'scikit-image'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
