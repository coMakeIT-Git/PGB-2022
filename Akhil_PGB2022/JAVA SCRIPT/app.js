function converterByte(y){
    document.getElementById("kb").value = y/1024;
    document.getElementById("mb").value = y/(1024*1024);
    document.getElementById("gb").value = y/(1024*1024*1024);
  }
  
  function converterKB(y){
    document.getElementById("Byte").value = y*1024;
    document.getElementById("mb").value = y/1024;
    document.getElementById("gb").value = y/(1024*1024);
  }
  
  function converterMB(y){
    document.getElementById("Byte").value = y*1024*1024;
    document.getElementById("kb").value = y*1024;
    document.getElementById("gb").value = y/1024;
  }

  function converterGB(y){
    document.getElementById("Byte").value = y*1024*1024*1024;
    document.getElementById("kb").value = y*1024*1024;
    document.getElementById("mb").value = y*1024;
  }