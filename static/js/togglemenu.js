var menuList = document.getElementById("menuList");

function togglemenu() {
    if(menuList.style.display == "none")
    {
        menuList.style.display = "flex";
        menuList.style.maxHeight = "190px";
    }
    else
    {
        menuList.style.display = "none";
        
    }
}