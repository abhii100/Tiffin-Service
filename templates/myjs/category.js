function getcategoryforcombo(myid = '') {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.responseText;
            var obj = JSON.parse(output);
            var s = "<option value=''>Choose</option>";
            var len = Object.keys(obj).length;
            for (var i = 0; i <= len - 1; i++) {
                s += "<option value='" + obj['dict' + i]['id'] + "'>" + obj['dict' + i]['cname'] + "</option>";
            }
            document.getElementById('categorycombo').innerHTML = s;
        }
        ;
    }
    xml.open("GET", "{% url 'viewcategorylist' %}", true);
    xml.send();
}

function addcategory() {
    if ($('#frm_addcategory').valid()) {
        var cname = document.getElementById('cname').value;
        var description = document.getElementById('description').value;
        var s = {
            'cname': cname,
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
                    document.getElementById("output").innerHTML = "Data already Exists";
                }
                else {
                    document.getElementById("output").innerHTML = "Data Not Inserted";
                }
            }
        };
        xml.open('GET', "{% url 'addcategoryaction' %}?dct=" + JSON.stringify(s), true);
        xml.send();
    }
}

function showcategorydataintable(obj) {
    var s = "<table class='table table-bordered'>" +
        "<tr>" +
        "<th width='70'>Srno</th>" +
        "<th>Category Name</th>" +
        "<th>Description</th>" +
        "<th width='200'>Action</th>" +
        "</tr>";
    var k = 1;
    var len = Object.keys(obj).length;
    for (var i = 0; i <= len - 1; i++) {
        s += "<tr>";
        s += "<th class='text-center'>" + k + "</td>";
        s += "<td>" + obj['dict' + i]['cname'] + "</td>";
        s += "<td>" + obj['dict' + i]['description'] + "</td>";
        s += "<td><a class='btn btn-warning' href={% url 'editcategorypage' %}?id=" + obj['dict' + i]['id'] + " >Edit</a> <a class='btn btn-danger' href='{% url 'deletecategory' %}?id=" + obj['dict' + i]['id'] + "'>Delete</a></td>";
        s += "</tr>";
        k++;
    }
    s = s + "</table>";
    document.getElementById('output').innerHTML = s;
}

function viewcategory() {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.responseText;
            var obj = JSON.parse(output);
            console.log(obj);
            showcategorydataintable(obj);
        }
    };
    xml.open('GET', "{% url 'viewcategorylist' %}", true);
    xml.send();
}

function categorybyid(id) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = JSON.parse(this.responseText)
            console.log(output);
            document.getElementById("cname").value = output['dict0']['cname'];
            document.getElementById("description").value = output['dict0']['description'];
        }
    };
    xml.open("GET", "{% url 'viewcategorybyid' %}?id=" + id, true);
    xml.send();
}

function editcategory() {
    if ($('#frm_editcategory').valid()) {
        var id = document.getElementById('id').value;
        var cname = document.getElementById('cname').value;
        var description = document.getElementById('description').value;
        var s = {'cname': cname, 'description': description, 'id': id};
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
        xml.open('GET', "{% url 'editcategoryaction' %}?dct=" + JSON.stringify(s), true);
        xml.send();
    }
}