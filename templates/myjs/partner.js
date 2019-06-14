function addgallery() {
    var formdata = new FormData();
    formdata.append('partnerid', document.getElementById('partnerid').value);
    formdata.append('photo', document.getElementById('photo').files[0]);
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.responseText;
            console.log(output);
            if (output == 1) {
                document.getElementById("output").innerHTML = "Data Inserted";
            }
            else {
                document.getElementById("output").innerHTML = "Data Not Inserted";
            }
        }
    };
    xml.open('POST', '/addgalleryaction', true);
    xml.send(formdata);
}


function addpartner() {
    if ($('#frm_addpartner').valid()) {
        var companyname = document.getElementById('companyname').value;
        var ownername = document.getElementById('ownername').value;
        var address = document.getElementById('address').value;
        var location = document.getElementById('location').value;
        var mobileno = document.getElementById('mobileno').value;
        var email = document.getElementById('email').value;
        var password = document.getElementById('password').value;
        location = location.replace(new RegExp('"', 'g'), '###');
        location = encodeURIComponent(location);
        // location = location.replace(new RegExp(' ', 'g'), '%20');
        // location = location.replace('+',"%20");
        // location = location.replace(new RegExp('+', 'g'), '%20');
        var s = {
            'companyname': companyname,
            'ownername': ownername,
            'address': address,
            'location': location,
            'mobileno': mobileno,
            'email': email,
            'password': password
        };
        console.log(JSON.stringify(s));
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
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
        xml.open('GET', "{% url 'signuppartneraction' %}?dct=" + JSON.stringify(s), true);
        xml.send();
    }
}

function showpartnerdataintable(obj) {
    var s = "<table class='table table-bordered'>" +
        "<tr>" +
        "<th>Srno</th>" +
        "<th>Company Name</th>" +
        "<th>Owner Name</th>" +
        "<th>Mobileno</th>" +
        "<th>Address</th>" +
        // "<th>Location</th>" +
        "<th>Email</th>" +
        "<th>Status</th>" +
        "<th width='120'>Action</th>" +
        "</tr>";
    var k = 1;
    var len = Object.keys(obj).length;
    for (var i = 0; i <= len - 1; i++) {
        s += "<tr>";
        s += "<th class='text-center'>" + k + "</td>";
        s += "<td>" + obj['dict' + i]['companyname'] + "</td>";
        s += "<td>" + obj['dict' + i]['ownername'] + "</td>";
        s += "<td>" + obj['dict' + i]['mobileno'] + "</td>";
        s += "<td>" + obj['dict' + i]['address'] + "</td>";
        // s += "<td>" + obj['dict' + i]['location'] + "</td>";
        s += "<td>" + obj['dict' + i]['email'] + "</td>";
        s += "<td>" + obj['dict' + i]['status'] + "</td>";
        if (obj['dict' + i]['status'] == 'Pending') {
            s += "<td><a class='btn btn-success' href={% url 'approverejectpartner' %}?id=" + obj['dict' + i]['id'] + "&status=Approved" + " >Approve</a> <a class='btn btn-danger' href='{% url 'approverejectpartner' %}?id=" + obj['dict' + i]['id'] + "&status=Rejected" + "'>Reject</a></td>";
        }
        else if (obj['dict' + i]['status'] == 'Approved') {
            s += "<td><a class='btn btn-danger' href='{% url 'approverejectpartner' %}?id=" + obj['dict' + i]['id'] + "&status=Rejected" + "'>Reject</a></td>";
        }
        else {
            s += "<td><a class='btn btn-success' href={% url 'approverejectpartner' %}?id=" + obj['dict' + i]['id'] + "&status=Approved" + " >Approve</a></td>";
        }
        s += "</tr>";
        k++;
    }
    s = s + "</table>";
    document.getElementById('output').innerHTML = s;
}

function viewpendingpartner() {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.responseText;
            var obj = JSON.parse(output);
            console.log(obj);
            showpartnerdataintable(obj);
        }
    };
    xml.open('GET', "{% url 'pendingpartnerlist' %}", true);
    xml.send();
}

function loginpartner() {
    if ($('#frm_loginpartner').valid()) {
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
                    window.location.href = "{% url 'partnerindex' %}";
                }
                else {
                    document.getElementById("output").innerHTML = "Invalid Login";
                }
            }
        };
        xml.open('GET', "{% url 'loginpartneraction' %}?dct=" + JSON.stringify(s), true);
        xml.send();
    }
}

function getpartnerbyid() {
    var id = document.getElementById('partnerid').value;
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.responseText;
            var obj = JSON.parse(output);
            // alert(obj['dict0']['companyname']);
            document.getElementById('companyname').innerHTML = obj['dict0']['companyname'];
            document.getElementById('companymobileno').innerHTML = "<strong>Mobile No.- </strong>" + obj['dict0']['mobileno'];
            document.getElementById('companyemail').innerHTML = "<strong>Email ID - </strong>" + obj['dict0']['email'];
            document.getElementById('companyaddress').innerHTML = obj['dict0']['address'];
        }
    };
    xml.open('GET', '/partnerforcustomerbyid?name=&id=' + id, true);
    xml.send();
}

function showmymap(id) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.responseText;
            var obj = JSON.parse(output);
            var location = obj['dict0']['location'];
            location = location.replace(new RegExp('###', 'g'), '"');
            location = decodeURIComponent(location);
            document.getElementById('partnermap').innerHTML = location;
        }
    };
    xml.open('GET', '/partnerforcustomerbyid?name=&id=' + id, true);
    xml.send();
}

function getallpartnerforcustomer() {
    var name = document.getElementById('searchpartner').value;
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.responseText;
            var obj = JSON.parse(output);
            console.log(obj);
            var len = Object.keys(obj).length;
            var s = "";
            var location = "";
            for (var i = 0; i <= len - 1; i++) {
                location = obj['dict0']['location'];
                location = location.replace(new RegExp('###', 'g'), '"');
                var k = obj['dict' + i]['id'];
                s += "<table class='table'>";
                s += "<tr class='address-tr'>" +
                    "<th width='20' class='heading'><span>" + (i + 1) + "</span></th>" +
                    "<td><a class='address-lnk' style='cursor:pointer;' onclick='showmymap(" + k + ")'><h6 class='companyname'>" + obj['dict' + i]['companyname'] + "</h6>" +
                    "<p>Contact Person - " + obj['dict' + i]['ownername'] + "</p>" +
                    "<p>Mobileno - " + obj['dict' + i]['mobileno'] + "</p>" +
                    "<p>Email ID - " + obj['dict' + i]['email'] + "</p>" +
                    "<p>Address - " + obj['dict' + i]['address'] + "</p></a>" +
                    "<br><a href='/showpartnermenu?id=" + k + "' class='btn' style='background-color: #502826;color:#fff;'>View Menu</a>&nbsp;&nbsp;" +
                    "</tr>";
                s += "</table>";
            }
            document.getElementById('partnerinfo').innerHTML = s;
            document.getElementById('partnermap').innerHTML = decodeURIComponent(location);
        }
    };
    xml.open('GET', "{% url 'allpartnerforcustomer' %}?name=" + name, true);
    xml.send();
}

function searchpartnerbyname() {
    var name = document.getElementById('searchpartner').value;
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.responseText;
            var obj = JSON.parse(output);
            console.log(obj);
            showpartnerdataintable(obj);
        }
    };
    xml.open('GET', "{% url 'partnerlistbyname' %}?name=" + name, true);
    xml.send();
}

function changepasswordpartner() {
    if ($('#frm_changepasswordpartner').valid()) {
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
                else if (output == 3) {
                    document.getElementById("output").innerHTML = "Invalid Old Password";
                }
                else {
                    document.getElementById("output").innerHTML = "Password Not Updated";
                }
            }
        };
        xml.open('GET', "{% url 'cp_partneraction' %}?dct=" + JSON.stringify(s), true);
        xml.send();
    }
}

function restorders(partnerid, status) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var ar = JSON.parse(this.response);
            var s = "";
            s += "<table class='table table-bordered'>";
            s += "<tr>";
            s += "<th>Srno.</th>";
            s += "<th>Order Date</th>";
            s += "<th>Customer</th>";
            s += "<th>Email</th>";
            s += "<th>Mobileno</th>";
            s += "<th>Address</th>";
            s += "<th>Amount</th>";
            s += "<th>Payment Via</th>";
            s += "<th>Details</th>";
            s += "</tr>";
            for (var i = 0; i < ar.length; i++) {
                s += "<tr>";
                s += "<td>" + (i + 1) + "</td>";
                s += "<td>" + ar[i]['dateoforder'] + "</td>";
                s += "<td>" + ar[i]['name'] + "</td>";
                s += "<td>" + ar[i]['email'] + "</td>";
                s += "<td>" + ar[i]['mobileno'] + "</td>";
                s += "<td>" + ar[i]['address'] + "</td>";
                s += "<td>" + ar[i]['amount'] + "</td>";
                s += "<td>" + ar[i]['paymentmode'] + "</td>";
                s += "<td><a href='/restorderdetailpage?orderid=" + ar[i]['orderid'] + "&mobileno=" + ar[i]['mobileno'] + "'>Order Detail</a></td>";
                s += "</tr>";
            }
            s += "</table>";
            document.getElementById('orderdiv').innerHTML = s;
        }
    };
    xml.open('GET', '/restorders?partnerid=' + partnerid + '&status=' + status, true);
    xml.send();
}

function restorderdetail(orderid, mobileno) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var ar = JSON.parse(this.response);
            var s = "";
            s += "<table class='table table-bordered'>";
            s += "<tr>";
            s += "<th>Srno.</th>";
            s += "<th>Item Name</th>";
            s += "<th>Price</th>";
            s += "<th>Qty</th>";
            s += "<th>Amount</th>";
            s += "</tr>";
            for (var i = 0; i < ar.length; i++) {
                s += "<tr>";
                s += "<td>" + (i + 1) + "</td>";
                s += "<td>" + ar[i]['itemname'] + "</td>";
                s += "<td>" + ar[i]['price'] + "</td>";
                s += "<td>" + ar[i]['qty'] + "</td>";
                s += "<td>" + ar[i]['amount'] + "</td>";
                s += "</tr>";
            }
            if (ar[0]['orderstatus'] == 'Pending') {
                s += "<tr>"
                s += "<td colspan='5' class='text-center'><a href='/accept_reject_order?orderid=" + ar[0]['orderid'] + "&status=Accepted&mobileno=" + mobileno + "' class='btn btn-success'>Accept Order</a> <a href='/accept_reject_order?orderid=" + ar[0]['orderid'] + "&status=Rejected&mobileno=" + mobileno + "' class='btn btn-danger'>Reject Order</a></td>"
                s += "</tr>"
            }
            s += "</table>";
            document.getElementById('orderdetaildiv').innerHTML = s;
        }
    };
    xml.open('GET', '/restorderdetail?orderid=' + orderid, true);
    xml.send();
}

function todaysales(partnerid) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var ar = JSON.parse(this.response);
            var chart = new CanvasJS.Chart("chartContainer", {
                animationEnabled: true,
                title: {
                    text: "Total Sales"
                },
                legend: {
                    cursor: "pointer",
                    itemclick: explodePie
                },
                data: [{
                    type: "pie",
                    showInLegend: true,
                    toolTipContent: "{name}: <strong>{y}%</strong>",
                    indexLabel: "{name} - Rs.{y}",
                    dataPoints: ar
                }]
            });
            chart.render();
        }
    };
    xml.open('GET', '/todaysales?partnerid=' + partnerid, true);
    xml.send();
}

function monthlysales(partnerid) {

    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var ar = JSON.parse(this.response);
            // alert(ar);
            // var chart = new CanvasJS.Chart("chartContainer1", {
            //     animationEnabled: true,
            //     theme: "light2", // "light1", "light2", "dark1", "dark2"
            //     title: {
            //         text: "Monthly Sales"
            //     },
            //     axisY: {
            //         title: "Sales(Rs.)"
            //     },
            //     data: [{
            //         type: "column",
            //         showInLegend: true,
            //         legendMarkerColor: "grey",
            //         legendText: "Date(YY-mm-dd)",
            //         dataPoints: ar
            //     }]
            // });

            var chart = new CanvasJS.Chart("chartContainer1", {
                title: {
                    text: "Monthly Sales"
                },
                axisY: {
                    title: "Sales(Rs.)",
                    prefix: "Rs."
                },
                data: [{
                    type: "column",
                    yValueFormatString: "Rs #,### ",
                    indexLabel: "{y}",
                    dataPoints: ar
                }]
            });
            chart.render();
        }
    };
    xml.open('GET', '/monthlysales?partnerid=' + partnerid, true);
    xml.send();
}

function explodePie(e) {
    if (typeof (e.dataSeries.dataPoints[e.dataPointIndex].exploded) === "undefined" || !e.dataSeries.dataPoints[e.dataPointIndex].exploded) {
        e.dataSeries.dataPoints[e.dataPointIndex].exploded = true;
    } else {
        e.dataSeries.dataPoints[e.dataPointIndex].exploded = false;
    }
    e.chart.render();

}