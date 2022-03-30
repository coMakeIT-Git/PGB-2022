
Steps:
    
    1.install visual studio code
    
      $ sudo dpkg code_1.65.2-1646927742_amd64.deb 
      
      or else install from ubuntu software ( code editing )
      
    2.install code runner in vs code
    
    3.install javscript(ES6)
    
    4. Html
    
    
   Ngnix Installatoin steps
   
   1. write following commands in terminals
   
   $ sudo apt update
   
   $ sudo apt install nginx
   
  (Adjusting the firewall)
   
   $ sudo ufw app list
   
        //OutputAvailable applications:
        Nginx Full
        Nginx HTTP
        Nginx HTTPS
        OpenSSH
        
   $ sudo ufw allow 'Nginx HTTP'
   
   $ sudo ufw status
   
   
         //OutputStatus: activeTo                         Action      From
                               --                         ------      ----
                             OpenSSH                    ALLOW       Anywhere                  
                             Nginx HTTP                 ALLOW       Anywhere                  
                             OpenSSH (v6)               ALLOW       Anywhere (v6)             
                             Nginx HTTP (v6)            ALLOW       Anywhere (v6)
                             
    
    (Checking your Web Server)
    
    $ systemctl status nginx
    
        //Output● nginx.service - A high performance web server and a reverse proxy server
        Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
        Active: active (running) since Fri 2018-04-20 16:08:19 UTC; 3 days ago
        Docs: man:nginx(8)
        Main PID: 2369 (nginx)
        Tasks: 2 (limit: 1153)
        CGroup: /system.slice/nginx.service
           ├─2369 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
           └─2380 nginx: worker process
   
   
   
     In firefox type  127.0.0.1 or type ur ip address
     
     
     (To start the Ngnix server)
     
     $ sudo systemctl start nginx
     
     (To stop and start the service again)
     
     $ sudo systemctl restart nginx
     
      
     (Create the directory for example.com as follows, using the -p flag to create any necessary parent directories)
     
     $ sudo mkdir -p /var/www/example.com/html
     
     (assign ownership of the directory with the $USER environment variable)
     
     $ sudo chown -R $USER:$USER /var/www/example.com/html
     
     location of var file : computer/var/www/example.com/html
     
     $ sudo nano /etc/nginx/sites-available/example.com
     
             server {
                      listen 80;
                      listen [::]:80;
                      
                      root /var/www/example.com/html;
                      index index.html index.htm index.nginx-debian.html;
                      
                      server_name example.com www.example.com;
                      
                      location / {
                                      try_files $uri $uri/ =404;
                        }
                     }
     
     
     $ sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/
     
     
     $ sudo nano /etc/nginx/nginx.conf
     
     	In nginx.conf file find the server_names_hash_bucket_size directive and remove the # symbol to uncomment the line:
     	
     	
            ...
               http {
                     ...
                         server_names_hash_bucket_size 64;
                     ...
                    }
            ...
     
     $ sudo nginx -t
   
   
     type url: 'localhost:80' in firefox
   
   
   post man install
   
   
   sudo snap install post man
   
   
   spring boot install
   
   (move file to opt folder)
   $ sudo mv spring-tool-suite-4-4.14.0.RELEASE-e4.23.0-linux.gtk.x86_64.tar.gz /opt/
   (extract spring tool )
   $ sudo tar -xvf spring-tool-suite-4-4.14.0.RELEASE-e4.23.0-linux.gtk.x86_64/
   
   $sudo nano /usr/share/applications/STS.desktop
   
   
   (paste the below data into sts.desktop)
   
   [Desktop Entry]
Name=SpringSource Tool Suite
Comment=Spring Tool Suite
Exec=/opt/sts-4.7.0.RELEASE/SpringToolSuite4
Icon=/opt/sts-4.7.0.RELEASE/icon.xpm
StartupNotify=true
Terminal=false
Type=Application
Categories=Development;IDE;Java;
   


   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
