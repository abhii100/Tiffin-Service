function getitemsforcombo(myid = '') {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.responseText;
            var obj = JSON.parse(output);
            var s = "<option value=''>Choose</option>";
            var len = Object.keys(obj).length;
            for (var i = 0; i <= len - 1; i++) {
                s += "<option value='" + obj['dict' + i]['id'] + "'>" + obj['dict' + i]['itemname'] + "</option>";
            }
            document.getElementById('itemcombo').innerHTML = s;
        }
        ;
    }
    xml.open("GET", "{% url 'viewfooditemlist' %}", true);
    xml.send();
}

function addfooditem() {
    if ($('#frm_addfoodmenu').valid()) {

        var categoryid = document.getElementById('categorycombo').value;
        var itemname = document.getElementById('itemname').value;
        var price = document.getElementById('price').value;
        var description = document.getElementById('description').value;
        var checkboxes = document.getElementsByName('days[]');
        var vals = "";
        for (var i = 0, n = checkboxes.length; i < n; i++) {
            if (checkboxes[i].checked) {
                vals += checkboxes[i].value + ",";
            }
        }
        // alert(vals);
        var n = vals.lastIndexOf(',');
        var availabledays = vals.substring(0, n);
        // alert(availabledays);
        var s = {
            'categoryid': categoryid,
            'itemname': itemname,
            'price': price,
            'description': description,
            'availabledays': [availabledays]
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
                    document.getElementById("output").innerHTML = "Data already Exists";
                }
                else {
                    document.getElementById("output").innerHTML = "Data Not Inserted";
                }
            }
        };
        xml.open('GET', "{% url 'addfooditemaction' %}?dct=" + JSON.stringify(s), true);
        xml.send();
    }
}


function getmenubypartner(partnerid) {
    var dt = document.getElementById('menudate').value;
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var s = "<table class='table'>";
            s += "<th colspan='4' class='text-center'><h3>Menu</h3></th>";
            s += "<tr>";
            s += "<th width='60'>Srno</th>";
            s += "<th>Item Name</th>";
            s += "<th width='150'>Price</th>";
            s += "<th width='150'>Action</th>";
            s += "</tr>";
            var output = this.responseText;
            // var obj = JSON.parse(output);
            // console.log(obj);
            // var len = Object.keys(obj).length;
            // for (var i = 0; i < len; i++) {
            //     s += "<tr>" +
            //         "<th>" + (i + 1) + "</th>" +
            //         "<td>" + obj['dict' + i]['itemname'] + "</td>" +
            //         "<td>Rs. " + obj['dict' + i]['price'] + "</td>" +
            //         "<td><button type='button' onclick='addtocart(" + obj['dict' + i]['id'] + ",1)' class='btn btn-success'>Add To Cart</button></td>" +
            //         "</tr>";
            // }
            // s += "<tr>";
            // s += "<td colspan='4' class='text-center'><a href='/allpartnerpage' class='btn btn-warning text-light'>Search Other Partner</a></td>";
            // s += "</tr>";
            // s += "</table>";
            document.getElementById('menuitemsoutput').innerHTML = output;
        }
    };
    xml.open('GET', '/getmenubypartner?partnerid=' + partnerid + '&myday=' + dt, true);
    xml.send();
}


function showfooditemdataintable(obj) {
    var s = "<table class='table table-bordered'>" +
        "<tr>" +
        "<th width='70'>Srno</th>" +
        "<th>Category</th>" +
        "<th>Item</th>" +
        "<th>Price</th>" +
        "<th>Available Days</th>" +
        "<th width='200'>Action</th>" +
        "</tr>";
    var k = 1;
    var len = Object.keys(obj).length;
    for (var i = 0; i <= len - 1; i++) {
        s += "<tr>";
        s += "<th class='text-center'>" + k + "</td>";
        s += "<td>" + obj['dict' + i]['cname'] + "</td>";
        s += "<td>" + obj['dict' + i]['itemname'] + "</td>";
        s += "<td>&#8377;" + obj['dict' + i]['price'] + "</td>";
        s += "<td>" + obj['dict' + i]['availabledays'] + "</td>";
        s += "<td><a class='btn btn-warning' href={% url 'editfooditempage' %}?id=" + obj['dict' + i]['id'] + " >Edit</a> <a class='btn btn-danger' href='{% url 'deletefooditem' %}?id=" + obj['dict' + i]['id'] + "'>Delete</a></td>";
        s += "</tr>";
        k++;
    }
    s = s + "</table>";
    document.getElementById('output').innerHTML = s;
}

function viewfooditem() {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.responseText;
            var obj = JSON.parse(output);
            // console.log(obj);
            showfooditemdataintable(obj);
        }
    };
    xml.open('GET', "{% url 'viewfooditemlist' %}", true);
    xml.send();
}

function getfooditembyid(id) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = JSON.parse(this.responseText)
            console.log(output);
            document.getElementById("itemname").value = output['dict0']['itemname'];
            document.getElementById("price").value = output['dict0']['price'];
            document.getElementById("description").value = output['dict0']['description'];
            document.getElementById("categorycombo").value = output['dict0']['categoryid'];
        }
    };
    xml.open("GET", "{% url 'viewfooditembyid' %}?id=" + id, true);
    xml.send();
}