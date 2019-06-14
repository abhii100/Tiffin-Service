function addcustomer() {
    if ($('#frm_addcustomer').valid()) {
        var url;
        var controls;
        var formdata = new FormData();
        url = "{% url 'signupcustomeraction' %}";
        controls = document.getElementById('frm_addcustomer').elements;
        for (var i = 0; i < controls.length; i++) {
            if (controls[i].type === "file") {
                if (controls[i].files.length > 0) {
                    formdata.append(controls[i].name, controls[i].files[0]);
                }
            }
            else {
                formdata.append(controls[i].name, controls[i].value);
            }
        }
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function () {
            //alert(this.status + ' ' + this.readyState);
            if (this.status == 200 && this.readyState == 4) {
                var output = this.responseText;
                console.log(output);
                if (output == 1) {
                    document.getElementById("output").innerHTML = "Data Inserted";
                }
                else if (output == 3) {
                    document.getElementById("output").innerHTML = "Email ID already Exists";
                }
                else {
                    document.getElementById("output").innerHTML = "Data Not Inserted";
                }
            }
        };
        xmlhttp.open("POST", url, true);
        xmlhttp.send(formdata);
    }
}

function logincustomer() {
    if ($('#frm_logincustomer').valid()) {
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
                if (len > 0) {
                    window.location.href = "{% url 'customerindex' %}";
                }
                else {
                    document.getElementById("output").innerHTML = "Invalid Login";
                }
            }
        };
        xml.open('GET', "{% url 'logincustomeraction' %}?dct=" + JSON.stringify(s), true);
        xml.send();
    }
}

function showcustomerdataintable(obj) {
    var s = "<table class='table table-bordered'>" +
        "<tr>" +
        "<th>Srno</th>" +
        "<th>Name</th>" +
        "<th>Mobileno</th>" +
        "<th>Address</th>" +
        "<th>Photo</th>" +
        "<th>Email</th>" +
        "<th>Action</th>" +
        "</tr>";
    var k = 1;
    var len = Object.keys(obj).length;
    for (var i = 0; i <= len - 1; i++) {
        s += "<tr>";
        s += "<th class='text-center'>" + k + "</td>";
        s += "<td>" + obj['dict' + i]['name'] + "</td>";
        s += "<td>" + obj['dict' + i]['mobileno'] + "</td>";
        s += "<td>" + obj['dict' + i]['address'] + "</td>";
        s += "<td><img src='../../static/upload/"+obj['dict'+i]['photo']+"' width='100' height='100' class='rounded-circle'></td>";
        s += "<td>" + obj['dict' + i]['email'] + "</td>";
        if(obj['dict' + i]['status']=='Pending')
        {
          s += "<td><a class='btn btn-success' href={% url 'approverejectcustomer' %}?id=" + obj['dict' + i]['id'] + "&status=Approved" + " >Approve</a> <a class='btn btn-danger' href='{% url 'approverejectcustomer' %}?id=" + obj['dict' + i]['id'] + "&status=Rejected" + "'>Reject</a></td>";
        }
        else if (obj['dict' + i]['status']=='Approved')
        {
            s += "<td><a class='btn btn-danger' href='{% url 'approverejectcustomer' %}?id=" + obj['dict' + i]['id'] + "&status=Rejected" + "'>Block</a></td>";
        }
        else
        {
            s += "<td><a class='btn btn-success' href={% url 'approverejectcustomer' %}?id=" + obj['dict' + i]['id'] + "&status=Approved" + " >UnBlock</a></td>";
        }
        s += "</tr>";
        k++;
    }
    s = s + "</table>";
    document.getElementById('output').innerHTML = s;
}

function viewpendingcustomer() {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.responseText;
            var obj = JSON.parse(output);
            console.log(obj);
            showcustomerdataintable(obj);
        }
    };
    xml.open('GET', "{% url 'pendingcustomerlist' %}", true);
    xml.send();
}

function searchcustomerbyname()
{
    var name = document.getElementById('searchcust').value;
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.responseText;
            var obj = JSON.parse(output);
            console.log(obj);
            showcustomerdataintable(obj);
        }
    };
    xml.open('GET', "{% url 'customerlistbyname' %}?name="+name, true);
    xml.send();
}

function changepasswordcustomer() {
    if ($('#frm_changepasswordcustomer').valid()) {
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
        xml.open('GET', "{% url 'cp_customeraction' %}?dct=" + JSON.stringify(s), true);
        xml.send();
    }
}

function myorders(customerid)
{
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function(){
        if(this.readyState == 4 && this.status==200)
        {
            var ar = JSON.parse(this.response);
            var s = "";
            s += "<table class='table table-bordered'>";
            s += "<tr>";
            s += "<th>Srno.</th>";
            s += "<th>Order Date</th>";
            s += "<th>Comapny</th>";
            s += "<th>Customer</th>";
            s += "<th>Email</th>";
            s += "<th>Mobileno</th>";
            s += "<th>Address</th>";
            s += "<th>Amount</th>";
            s += "<th>Payment Via</th>";
            s += "</tr>";
            for(var i=0;i<ar.length;i++)
            {
                s += "<tr>";
                s += "<td>"+(i+1)+"</td>";
                s += "<td>"+ar[i]['dateoforder']+"</td>";
                s += "<td>"+ar[i]['companyname']+"</td>";
                s += "<td>"+ar[i]['name']+"</td>";
                s += "<td>"+ar[i]['email']+"</td>";
                s += "<td>"+ar[i]['mobileno']+"</td>";
                s += "<td>"+ar[i]['address']+"</td>";
                s += "<td>"+ar[i]['amount']+"</td>";
                s += "<td>"+ar[i]['paymentmode']+"</td>";
                s += "</tr>";
            }
            s += "</table>";
            document.getElementById('orderdiv').innerHTML = s;
        }
    };
    xml.open('GET','/myorders?customerid='+customerid,true);
    xml.send();
}