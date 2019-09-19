function getXMLHttpRequest() {
    var xhr = null;
    try
    {
    xhr = new ActiveXObject("Microsoft.XMLHTTP Microsoft.XMLHTTP"); // Essayer IE "); // Essayer IE
    }
    catch(e) // Echec, utiliser l'objet standard
    {
    xhr = new XMLHttpRequest();
    }
    return xhr;
    }