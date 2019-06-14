
function loginadmin()
{
    // alert();
    if ($('#frm_loginadmin').valid()) {
        var email = document.getElementById('email').value;
        var password = document.getElementById('password').value;
        var s = {
            'email': email,
            'password': password
        };
        console.log(s);
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var output = this.responseText;
                var obj = JSON.parse(output);
                console.log(obj);
                var len = Object.keys(obj).length;
                if (len>0) {
                    window.location.href = "{% url 'adminindex' %}";
                }
                else {
                    document.getElementById("output").innerHTML = "Invalid Login";
                }
            }
        };
        xml.open('GET', "{% url 'loginadminaction' %}?dct=" + JSON.stringify(s), true);
        xml.send();
    }
}

function changepasswordadmin() {
    if ($('#frm_changepasswordadmin').valid()) {
        var email = document.getElementById('email').value;
        var oldpassword = document.getElementById('oldpassword').value;
        var newpassword = document.getElementById('newpassword').value;
        var cpassword = document.getElementById('cpassword').value;
        var s = {'email': email, 'oldpassword': oldpassword, 'newpassword': newpassword};
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var output = this.responseText;
                console.log(output);
                if (output == 1) {
                    document.getElementById("output").innerHTML = "Password Updated Successfully";
                }
                else if (output==3)
                {
                    document.getElementById("output").innerHTML = "Invalid Old Password";
                }
                else {
                    document.getElementById("output").innerHTML = "Password Not Updated";
                }
            }
        };
        xml.open('GET', "{% url 'cp_adminaction' %}?dct=" + JSON.stringify(s), true);
        xml.send();
    }
}