import os

import uvicorn
from dotenv import load_dotenv

import forge.sdk.forge_log

LOG = forge.sdk.forge_log.ForgeLogger(__name__)


logo = """\n\n                                                                                                                                            
                                                                                                         ░░░░░░░░░░░░░░                      
   SSSSSSSSSSSSSSS                                                                                     ░░░░░░░░░░░░░░░░░░                    
 SS:::::::::::::::S                                                                                  ▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒░░░░                  
S:::::SSSSSS::::::S                                                                                ▒▒▒▒    ▒▒▒▒▒▒    ▒▒▒▒░░░░                
S:::::S     SSSSSSS                                                                                ▒▒    ██  ▒▒  ██    ▒▒████                
S:::::S            uuuuuu    uuuuuu      ssssssssss     aaaaaaaaaaaaa  nnnn  nnnnnnnn              ▒▒        ▒▒        ▒▒████                
S:::::S            u::::u    u::::u    ss::::::::::s    a::::::::::::a n:::nn::::::::nn            ▒▒▒▒    ▒▒▒▒▒▒    ▒▒▒▒░░░░    ▒▒    ▒▒    
 S::::SSSS         u::::u    u::::u  ss:::::::::::::s   aaaaaaaaa:::::an::::::::::::::nn           ░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒░░░░░░    ▒▒▒▒▒▒      
  SS::::::SSSSS    u::::u    u::::u  s::::::ssss:::::s           a::::ann:::::::::::::::n          ░░░░░░░░░░░░░░░░░░░░░░░░░░    ▒▒▒▒▒▒▒▒▒▒  
    SSS::::::::SS  u::::u    u::::u   s:::::s  ssssss     aaaaaaa:::::a  n:::::nnnn:::::n          ░░░░░░░░░░░░░░░░░░░░░░░░░░    ▒▒▒▒▒▒▒▒    
       SSSSSS::::S u::::u    u::::u     s::::::s        aa::::::::::::a  n::::n    n::::n          ░░░░░░░░░░░░░░██░░░░░░░░░░    ▒▒▒▒▒▒▒▒▒▒▒▒
            S:::::Su::::u    u::::u        s::::::s    a::::aaaa::::::a  n::::n    n::::n          ░░░░░░░░██████░░░░░░░░░░░░  ▒▒▒▒▒▒▒▒▒▒▒▒░░
            S:::::Su:::::uuuu:::::u  ssssss   s:::::s a::::a    a:::::a  n::::n    n::::n          ░░░░░░░░░░░░░░░░░░░░██████  ▒▒▒▒▒▒        
SSSSSSS     S:::::Su:::::::::::::::uus:::::ssss::::::sa::::a    a:::::a  n::::n    n::::n        ░░████░░░░  ░░░░██████████░░░░▒▒▒▒          
S::::::SSSSSS:::::S u:::::::::::::::us::::::::::::::s a:::::aaaa::::::a  n::::n    n::::n      ░░░░██████      ██████████░░░░░░░░            
S:::::::::::::::SS   uu::::::::uu:::u s:::::::::::ss   a::::::::::aa:::a n::::n    n::::n      ░░░░██████████████████████░░██░░░░            
 SSSSSSSSSSSSSSS       uuuuuuuu  uuuu  sssssssssss      aaaaaaaaaa  aaaa nnnnnn    nnnnnn      ░░░░                          ░░              
                                                                                                 ░░████          ████████████                
                                                                                   v0.0.4          ██              ██████████                
                                                                                                 ████              ████████████              
                                                                                               ████████          ████████████████            
                                                                                             ████████████████████████████                    
                                                                                                 ████████████                                
                                                                                                               ▒▒▒▒                          
                                                                                                         ▒▒▒▒  ▒▒▒▒                          
                                                                                                       ██████  ██████                        
                                                                                                                                             
\n"""

if __name__ == "__main__":
    print(logo)
    port = os.getenv("PORT", 8000)
    LOG.info(f"Agent server starting on http://localhost:{port}")
    load_dotenv()
    forge.sdk.forge_log.setup_logger()

    uvicorn.run(
        "forge.app:app", host="localhost", port=port, log_level="error", reload=True
    )
