function addtocart(itemid = '', itemqty = '') {

    // if ($('#frm_addtocart').valid()) {
    var id, qty;
    if (itemid == '') {
        id = document.getElementById('itemcombo').value;
    }
    else {
        id = itemid;
    }
    if (itemqty == '') {
        qty = document.getElementById('qty').value;
    }
    else {
        qty = itemqty;
    }

    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.responseText;
            // alert(output);
            $('#cartmodal').modal();
            // var output = JSON.parse(this.responseText);
            // console.log(output);
            // var obj = output;
            // var len = Object.keys(obj).length;
            // var s = "<table class='table table-bordered'>";
            // s +="<tr>";
            // s += "<th>Srno</th>";
            // s += "<th>Item Name</th>";
            // s += "<th>Price</th>";
            // s += "<th>Qty</th>";
            // s += "<th>Amount</th>";
            // s +="</tr>";
            // for (var i = 0; i <= len - 1; i++) {
            //     var ar = obj['dct'+i];
            //      s += "<tr>";
            //      s += "<td>"+(i+1)+"</td>";
            //      s += "<td>"+ar['itemname']+"</td>";
            //      s += "<td>"+ar['price']+"</td>";
            //      s += "<td>"+ar['qty']+"</td>";
            //      s += "<td>"+ar['total']+"</td>";
            //      s += "</tr>";
            // }
            // s += "</table>";
            // document.getElementById('carttable').innerHTML = output;
            // console.log(output);
            // var ss = output.split('$$$$$');
            // document.getElementById('carttable').innerHTML = ss[0];
            // document.getElementById('cartcount').innerHTML = "("+ss[1]+")";
            // alert("("+ss[1]+")");
        }
    };
    xml.open('GET', '/addtocartpage1?id=' + id + "&qty=" + qty, true);
    xml.send();
    // }
}

function getcartitems() {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.responseText;
            // var ss = output.split('$$$$$');
            document.getElementById('carttable').innerHTML = output;
            // document.getElementById('cartcount').innerHTML = "("+ss[1]+")";
        }
    };
    xml.open('GET', '/getcartitemsintable', true);
    xml.send();
}

function deletefromcart(itemid) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState = 4 && this.status == 200) {
            var output = this.responseText;
            console.log(output);
            document.getElementById('carttable').innerHTML = output;
        }
    };
    xml.open('GET', '/deletefromcart?id=' + itemid, true);
    xml.send();
}
