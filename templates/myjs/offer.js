function addoffer() {
    if ($('#frm_addoffer').valid()) {
        var offername = document.getElementById('offername').value;
        var rate = document.getElementById('rate').value;
        var fromdate = document.getElementById('fromdate').value;
        var todate = document.getElementById('todate').value;
        var description = encodeURIComponent(document.getElementById('description').value);
        var s = {
            'offername': offername,
            'rate': rate,
            'fromdate': fromdate,
            'todate': todate,
            'description': description
        };
        console.log(s);
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
        xml.open('GET', "{% url 'addofferaction' %}?dct=" + JSON.stringify(s), true);
        xml.send();
    }
}

function showofferdataintable(obj) {
    var s = "<table class='table table-bordered'>" +
        "<tr>" +
        "<th>Srno</th>" +
        "<th>Offer Name</th>" +
        "<th>Rate</th>" +
        "<th>Start Date</th>" +
        "<th>End Date</th>" +
        "<th>Action</th>" +
        "</tr>";
    var k = 1;
    var len = Object.keys(obj).length;
    for (var i = 0; i <= len - 1; i++) {
        s += "<tr>";
        s += "<th class='text-center'>" + k + "</td>";
        s += "<td>" + obj['dict' + i]['offername'] + "</td>";
        s += "<td>" + obj['dict' + i]['rate'] + "</td>";
        s += "<td>" + obj['dict' + i]['fromdate'] + "</td>";
        s += "<td>" + obj['dict' + i]['todate'] + "</td>";
        s += "<td><a class='btn btn-warning' href={% url 'editofferpage' %}?id=" + obj['dict' + i]['id'] + " >Edit</a> <a class='btn btn-danger' href='{% url 'deleteoffer' %}?id=" + obj['dict' + i]['id'] + "'>Delete</a></td>";
        s += "</tr>";
        k++;
    }
    s = s + "</table>";
    document.getElementById('output').innerHTML = s;
}

function viewoffer() {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.responseText;
            var obj = JSON.parse(output);
            console.log(obj);
            showofferdataintable(obj);
        }
    };
    xml.open('GET', "{% url 'viewofferlist' %}", true);
    xml.send();
}

function searchofferbydate() {
    var fromdate = document.getElementById('searchfromdate').value;
    var todate = document.getElementById('searchtodate').value;
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.responseText;
            var obj = JSON.parse(output);
            console.log(obj);
            showofferdataintable(obj);
        }
    };
    xml.open('GET', "{% url 'offerlistbydate' %}?fromdate=" + fromdate.toString() + "&todate=" + todate.toString(), true);
    xml.send();
}

function offerbyid(id) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = JSON.parse(this.responseText)
            console.log(output);
            document.getElementById("offername").value = output['dict0']['offername'];
            document.getElementById("rate").value = output['dict0']['rate'];
            document.getElementById("fromdate").value = output['dict0']['fromdate'];
            document.getElementById("todate").value = output['dict0']['todate'];
            document.getElementById("description").value = output['dict0']['description'];
        }
    };
    xml.open("GET", "{% url 'viewofferbyid' %}?id=" + id, true);
    xml.send();
}

function editoffer() {
    if ($('#frm_editoffer').valid()) {
        var id = document.getElementById('id').value;
        var offername = document.getElementById('offername').value;
        var rate = document.getElementById('rate').value;
        var fromdate = document.getElementById('fromdate').value;
        var todate = document.getElementById('todate').value;
        var description = encodeURIComponent(document.getElementById('description').value);
        var s = {
            'offername': offername,
            'rate': rate,
            'fromdate': fromdate,
            'todate': todate,
            'description': description,
            'id': id
        };
        console.log(s);
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var output = this.responseText;
                console.log(output);
                if (output == 1) {
                    document.getElementById("output").innerHTML = "Data Updated";
                }
                else {
                    document.getElementById("output").innerHTML = "Data Not Updated";
                }
            }
        };
        xml.open('GET', "{% url 'editofferaction' %}?dct=" + JSON.stringify(s), true);
        xml.send();
    }
}