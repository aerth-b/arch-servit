#!/usr/bin/env python2
########################
# ALL RIGHTS RESERVED
#
# (c)2015
#
# MIT LICENSE
#
# SERVIT VERSION 1.070515
#
# Contributors: aerth
#
########################
#!/usr/bin/env python
from os import system
import curses, sys, traceback, os, logging
def main():
    try:
        def get_param(prompt_string):
            screen.clear()
            screen.border(0)
            screen.addstr(2, 2, prompt_string)
            screen.refresh()
            screen.addstr(1, 2, "EARTHBOT SERVIT [archlinux]", curses.A_STANDOUT)
            input = screen.getstr(10, 10, 600)
            return input
        def get_params(prompt_string, second_string):
            screen.clear()
            screen.border(0)
            screen.addstr(2, 10, prompt_string)
            screen.addstr(4, 10, second_string)
            screen.refresh()
            screen.addstr(1, 2, "EARTHBOT SERVIT [archlinux]", curses.A_STANDOUT)
            input = screen.getstr(10, 10, 60)
            return input
        def execute_cmd(cmd_string):
            system("reset")
            a = system(cmd_string)
            if a == 0:
                print("Command executed correctly")
            else:
                print("Command terminated with error")
            raw_input("Press enter")
            #system("reset")
        def launch_cmd(cmd_string):
            system("reset")
            a = system(cmd_string)
            print("")
            if a == 0:
                print("Command executed correctly")
            else:
                print("Command terminated with error")
            raw_input("Press enter")
            #x = ord('q')
            #print ""
            #system("reset")
        x = 0
        while x != ord('q'):
            system("reset")
            logging.debug('LOL we fired it up!')
            screen = curses.initscr()
            SCREEN_HEIGHT, SCREEN_WIDTH = screen.getmaxyx()
            screen.clear()
            screen.border(0)
            curses.start_color()
            curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
            curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
            curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)
            curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
            curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)
            screen.bkgd(' ', curses.color_pair(4))
            pos = 2
            curses.cbreak()
            curses.noecho()
            screen.keypad(0)
            screen.refresh()
            screen.addstr(1, 2, "EARTHBOT SERVIT", curses.A_STANDOUT)
            screen.addstr(2,2, "Please choose your journey...  ", curses.A_BOLD)
            screen.addstr(5, 2, "Web Server", curses.color_pair(4))
            screen.addstr(7, 2, "1 - Install Dependencies", curses.color_pair(2))
            screen.addstr(8, 2, "2 - systemctl httpd restart", curses.color_pair(2))
            screen.addstr(9, 2, "3 - Disk Free Space (df -h)", curses.color_pair(2))
            screen.addstr(10, 2, "4 - Show disk usage / (ncdu /)", curses.color_pair(2))
            screen.addstr(11, 2, "$ - Show disk usage . (ncdu .)", curses.color_pair(2))
            screen.addstr(12, 2, "5 - Show mounted spaces", curses.color_pair(2))
            screen.addstr(13, 2, "6 - TCPDUMP")
            screen.addstr(14, 2, "7 - Create Apache VHost", curses.color_pair(2))
            screen.addstr(15, 2, "8 - journalctl -xe", curses.color_pair(2))
            screen.addstr(16, 2, "` - Create Subdomain", curses.color_pair(2))
            screen.addstr(17, 2, "w - Backup Something")
            screen.addstr(18, 2, "e - Backup All")
            screen.addstr(19, 2, "r - ASCII art (figlet)")
            screen.addstr(20, 2, "t - Web Browser (w3m)", curses.color_pair(2))
            screen.keypad(1)
            screen.addstr(2, 50, "Press q or CTRL + C to Exit")
            screen.addstr(1, 30, "Made for ARCH LINUX WORLD DOMINATION, INC")
            s = curses.newwin(1, 15, 2, 8)
            curses.noecho()
            s.box()
            #screen.refresh()
            x = screen.getch()
            if x == ord('1'):
                confirm = get_params("Downloading and installing dependencies!","Are you sure?  type yes")
                curses.endwin()
                if confirm == "yes":
                    logging.debug('Installing Dependencies')
                    execute_cmd("sudo pacman -S git wget curl zsh figlet ufw ncdu tree multitail")
            if x == ord('2'):
                curses.endwin()
                logging.debug('Restarting httpd')
                execute_cmd("sudo systemctl restart httpd")
            if x == ord('3'):
                curses.endwin()
                execute_cmd("sudo df -h | less")
            if x == ord('4'):
                curses.endwin()
                execute_cmd("sudo ncdu /")
            if x == ord('$'):
                curses.endwin()
                execute_cmd("sudo ncdu .")
            if x == ord('5'):
                curses.endwin()
                execute_cmd("mount | less")
            if x == ord('6'):
                iface = get_param("Which network interface? (eth0 or wlan0 ?)")
                curses.endwin()
                execute_cmd("sudo tcpdump -vv -i " + iface )
            if x == ord('7'):
                sitedomain = get_param("Enter the domain name (example.com)")
                curses.endwin()
                logging.debug('making new domain name: ' + sitedomain)
                execute_cmd("sudo httpd-createsite " + sitedomain)
            if x == ord('8'):
                curses.endwin()
                execute_cmd("journalctl -xe")
            if x == ord('w'):
                backupsite = get_params("If site is located in /srv/live/example.com/public_html/","Enter only: example.com")
                confirm = get_param("Are you sure? backing up /srv/live/" + backupsite)
                curses.endwin()
                if confirm == "yes":
                   execute_cmd("echo tar czf /tmp/backup_" + backupsite + ".tar.gz /srv/live/" + backupsite + "/public_html")
            if x == ord('e'):
                confirm = get_param("Are you sure? backing up /srv/live/")
                curses.endwin()
                if confirm == "yes":
                   execute_cmd("sudo tar czf -p /tmp/backup_allsites.tar.gz /srv/live/")
            if x == ord('w'):
                confirm = get_param("Are you sure? backing up /srv/live/")
                curses.endwin()
                if confirm == "yes":
                   execute_cmd("echo tar czf -p /tmp/backup_allsites.tar.gz /srv/live/")
                   #execute_cmd("sudo ncdu .")
            if x == ord('r'):
                banner = get_param("Enter text to change into art")
                curses.endwin()
                execute_cmd("figlet " + banner)
            if x == ord('t'):
                url = get_param("Enter URL to surf to")
                curses.endwin()
                execute_cmd("w3m " + url)
            if x == ord('p'):
                sitedomain = get_param("Enter only the domain name (/srv/live/example.com/public_html)")
                curses.endwin()
                execute_cmd("sudo mv /srv/live" + sitedomain + "/public_html/index.html /tmp/index." + sitedomain + ".html")
                execute_cmd("sudo git clone /usr/share/grav-skel/ /srv/live/"  + sitedomain + "/public_html/")
                execute_cmd("cd /srv/live"  + sitedomain + "/public_html/")
                execute_cmd("sudo chown www-data:www:data/srv/live/"  + sitedomain + "/public_html/ -R")
            if x == ord('a'):
                hostname = get_param("SSH to Server: [hostname]")
                username = get_param("SSH to Server: [username]")
                xfor = get_param("SSH to Server: [x-forwarding] (yes/no)")
                port = get_param("SSH to Server: [port]")
                identity = get_param("SSH to Server: [path to: public key]")
                curses.endwin()
                if xfor == "yes":
                   xfora = " -X "
                else:
                   xfora = " "
                if identity == "":
                   identitya = ""
                else:
                   identitya == " -i " + identity
                if port == "":
                   porta = ""
                else:
                   porta = " -p " + port
                execute_cmd("ssh " + xfora + username + "@" + hostname + porta + identitya + " -v")
            if x == ord('s'):
                hostname = get_param("SCP to Server: [hostname]")
                username = get_param("SCP to Server: [username]")
                port = get_param("SCP to Server: [port]")
                identity = get_param("SCP to Server: [path to: public key]")
                filesend = get_param("SCP to Server: [files to send]")
                curses.endwin()
                if identity == "":
                   identitya = ""
                else:
                   identitya == " -i " + identity
                if port == "":
                   porta = ""
                else:
                   porta = " -P " + port + " "
                execute_cmd("scp -v " + porta + filesend + " " + username + "@" + hostname + ":~/ " + identitya)
            if x == ord('f'):
                execute_cmd("sudo pacman -S zsh")
            if x == ord('g'):
                execute_cmd("curl -L https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh | sh")
            if x == ord('h'):
                execute_cmd("curl -sS https://getcomposer.org/installer | php")
            if x == ord('j'):
                execute_cmd("sudo ufw default DENY;sudo ufw start;sudo systemctl start ufw;sudo systemctl enable ufw;sudo ufw status numbered")
            if x == ord(';'):
                portallow = get_param("Which port to allow? (careful!)")
                launch_cmd("sudo ufw allow " + portallow)
            if x == ord('/'):
                hostban = get_param("Which HOST to BAN? 20.200.20.200/24 (careful!)")
                execute_cmd("sudo ufw insert 1 deny " + hostban)
            if x == ord('K'):
                execute_cmd("sudo ufw default DENY")
            if x == ord('L'):
                execute_cmd("sudo ufw status")
            if x == ord(':'):
                whiteallow = get_param("Which IP to whitelist? (careful!)")
                execute_cmd("sudo ufw allow from " + whiteallow)
                execute_cmd("sudo echo \" + whiteallow + \" >> /etc/hosts.allow")
            if x == ord('?'):
                blackdeny = get_param("Which IP to blacklist? (careful!)")
                execute_cmd("sudo ufw deny from " + blackdeny)
                execute_cmd("sudo echo \" + blackdeny + \" >> /etc/hosts.deny")
            if x == ord('z'):
                execute_cmd("sudo who | less")
            if x == ord('x'):
                execute_cmd("sudo tail -f /var/log/apache2/access.log | less")
            if x == ord('c'):
                execute_cmd("sudo multitail -f /var/log/apache2/access.log /var/log/apache2/other-vhosts-access.log /var/log/apache2/error.log")
            if x == ord('v'):
                execute_cmd("sudo multitail -f /var/log/auth.log /var/log/dmesg.log /var/log/fail2ban.log /var/log/ufw.log")
            if x == ord('m'):
                execute_cmd("sudo htop")
            if x == ord(','):
                execute_cmd("inxi -Fxz")
            if x == ord('.'):
                execute_cmd("sudo last | less")
            if x == ord('!'):
                execute_cmd("sudo pacman -Syy; sudo pacman -Syu")
            if x == ord('@'):
                execute_cmd("sudo ps aux | less")
            if x == ord('#'):
                endit = get_param("What is the name of the process to end?")
                execute_cmd("sudo pkill " + endit)
        curses.endwin()
    except KeyboardInterrupt:
        print("\n Have a Grateful Day! :D \n")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    os.system('reset')
if __name__ == "__main__":
    logging.basicConfig(
        level = logging.DEBUG,
        format="[%(levelname)-8s] %(asctime)s %(module)s:%(lineno)d %(message)s",
        datefmt="%H:%M:%S",
        filename = '/tmp/servit-arch.log',
        #filename = './tmp-servit-arch.log',
        filemode = 'w'
    )
    main()
