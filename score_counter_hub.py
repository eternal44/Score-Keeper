'''this program pulls in modules and sequences them'''

from login import login, setup_account
from menu_selections import print_menu

setup_account()
login()
print_menu()
login()

