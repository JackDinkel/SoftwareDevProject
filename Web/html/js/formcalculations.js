/*
This source is shared under the terms of LGPL 3
www.gnu.org/licenses/lgpl.html

You are free to use the code in Commercial or non-commercial projects
*/

 //Set up an associative array
 //The keys represent the size of the cake
 //The values represent the cost of the cake i.e A 10" cake cost's $35
 var cake_prices = new Array();
 cake_prices["Round6"]=20;
 cake_prices["Round8"]=25;
 cake_prices["Round10"]=35;
 cake_prices["Round12"]=75;
 
 //Set up an associative array 
 //The keys represent the filling type
 //The value represents the cost of the filling i.e. Lemon filling is $5,Dobash filling is $9
 //We use this this array when the user selects a filling from the form
 var filling_prices= new Array();
 filling_prices["None"]=0;
 filling_prices["Lemon"]=5;
 filling_prices["Custard"]=5;
 filling_prices["Fudge"]=7;
 filling_prices["Mocha"]=8;
 filling_prices["Raspberry"]=10;
 filling_prices["Pineapple"]=5;
 filling_prices["Dobash"]=9;
 filling_prices["Mint"]=5;
 filling_prices["Cherry"]=5;
 filling_prices["Apricot"]=8;
 filling_prices["Buttercream"]=7;
 filling_prices["Chocolate Mousse"]=12;
 
	 
	 
// getCakeSizePrice() finds the price based on the size of the cake.
// Here, we need to take user's the selection from radio button selection
function getCakeSizePrice()
{  
    var cakeSizePrice=0;
    //Get a reference to the form id="form"
    var theForm = document.forms["form"];
    //Get a reference to the cake the user Chooses name=selectedCake":
    var selectedCake = theForm.elements["selectedcake"];
    //Here since there are 4 radio buttons selectedCake.length = 4
    //We loop through each radio buttons
    for(var i = 0; i < selectedCake.length; i++)
    {
        //if the radio button is checked
        if(selectedCake[i].checked)
        {
            //we set cakeSizePrice to the value of the selected radio button
            //i.e. if the user choose the 8" cake we set it to 25
            //by using the cake_prices array
            //We get the selected Items value
            //For example cake_prices["Round8".value]"
            cakeSizePrice = cake_prices[selectedCake[i].value];
            //If we get a match then we break out of this loop
            //No reason to continue if we get a match
            break;
        }
    }
    //We return the cakeSizePrice
    return cakeSizePrice;
}

//This function finds the filling price based on the 
//drop down selection
function getFillingPrice()
{
    var cakeFillingPrice=0;
    //Get a reference to the form id="form"
    var theForm = document.forms["form"];
    //Get a reference to the select id="filling"
     var selectedFilling = theForm.elements["filling"];
     
    //set cakeFilling Price equal to value user chose
    //For example filling_prices["Lemon".value] would be equal to 5
    cakeFillingPrice = filling_prices[selectedFilling.value];

    //finally we return cakeFillingPrice
    return cakeFillingPrice;
}

//candlesPrice() finds the candles price based on a check box selection
function candlesPrice()
{
    var candlePrice=0;
    //Get a reference to the form id="form"
    var theForm = document.forms["form"];
    //Get a reference to the checkbox id="includecandles"
    var includeCandles = theForm.elements["includecandles"];

    //If they checked the box set candlePrice to 5
    if(includeCandles.checked==true)
    {
        candlePrice=5;
    }
    //finally we return the candlePrice
    return candlePrice;
}

function insciptionPrice()
{
    //This local variable will be used to decide whether or not to charge for the inscription
    //If the user checked the box this value will be 20
    //otherwise it will remain at 0
    var inscriptionPrice=0;
    //Get a refernce to the form id="form"
    var theForm = document.forms["form"];
    //Get a reference to the checkbox id="includeinscription"
    var includeInscription = theForm.elements["includeinscription"];
    //If they checked the box set inscriptionPrice to 20
    if(includeInscription.checked==true){
        inscriptionPrice=20;
    }
    //finally we return the inscriptionPrice
    return inscriptionPrice;
}
        
/*function calculateTotal()
{
    //Here we get the total price by calling our function
    //Each function returns a number so by calling them we add the values they return together
    //var cakePrice = getCakeSizePrice() + getFillingPrice() + candlesPrice() + insciptionPrice();
    
    //display the result
    var divobj = document.getElementById('totalPrice');
    divobj.style.display='block';
    divobj.innerHTML = "Total Price For the Cake $10";

}*/

var buttonList = ["contract", "used", "insurance", "power", "water", "box"]

/*
 *************NOTES******************
 *contract coefficient:
 *  yes: 1
 *  no: 0
 *used coefficient:
 *  yes: 1
 *  no: full phone price - exit
 *insurance coefficient:
 *  yes: 1.5
 *  no: 1
 *power coefficient:
 *  yes: 1
 *  no: .25
 *water coefficient:
 *  yes: .7
 *  no: 1
 *box coefficient:
 *  yes: add $5
 *  no: 1
 ************************************
 */


var yes_no_list = new Array();
    yes_no_list["yes"] = 1;
    yes_no_list["no"] = 0;

function manufacturer()
{
    var manufacturer_coefficient = 1;

    //build an array with the values
    var manufacturerList = new Array();
    manufacturerList["Samsung"]=1;
    manufacturerList["LG"]=1;
    manufacturerList["HTC"]=1;
    manufacturerList["Apple"]=1;

    var form = document.forms["form"];
    var manufacturer = form.elements["manufacturer"];

    //loop through the buttons
    for(var i = 0; i < manufacturer.length; i++)
    {
        //if the radio button is checked
        if(manufacturer[i].checked)
        {
            //retrieve the value from the array
            manufacturer_coefficient = manufacturerList[manufacturer[i].value];
            //if there is a match, break, since only one button can be checked
            break;
        }
    }
    //return the value
    return manufacturer_coefficient;
}

function readbuttons(buttontype, list)
{
    /*
     * This function is meant to be used on buttons. It will check
     * if a button is checked and cross reference that with a 
     * hard coded list (above) to find the correct value to return.
     * The return value is a coefficient to be multiplied into the
     * total phone price.
     *
     * Eventually, it would be nice to have some sort of functionality
     * where the list is not hard coded but rather imported, either
     * from a formatted document, a database of some sort, or perhaps
     * I could write a python scrip that will generate a JavaScript
     * file from one of the other two.
     *
     * The function takes two arguments
     *      1. buttontype: the name of the button from the html
     *         document - examples: "contract", "used", "power"
     *      2. list: the name of the list containing to coefficients
     *         to which the buttons correspond
     */

    //the multiplier to return
    var coefficient = 1;

    var form = document.forms["form"]; //selecting the html file
    var buttonList = form.elements[buttontype]; //selecting which buttons to use

    //loop through each button until a checked one is found
    //if it is checked, we can break, since no others will be checked
    for (var i = 0; i < buttonList.length; i++)
    {
        if(buttonList[i].checked)
        {
            coefficient = list[buttonList[i].value]; //consult the appropriate list to
            break;                                   //  find the correct coefficient
        }
    }
    return coefficient;
}

function hideTotal()
{
    /*
     * This simple function can be called to make the total price at
     * the bottom of the form not be displayed. It is intended to be
     * used at the beginning so that the total is not shown until
     * some sort of calculation has been performed, but it could also
     * be used in case of error, or other purposes.
     */

    var divobj = document.getElementById('totalPrice'); //grab the totalPrice element
    divobj.style.display='none'; //set it to not display
}

function calculateTotal()
{
    /*
     * This function calculates the total price from the inputs
     * and displays the results in the element 'totalPrice'.
     * This is intended to be called repeatedly after each change
     * or input to the form so that the displayed price is always
     * as updated and accurate as possible.
     */

    var totalprice = manufacturer(); //test line - this will be replaced

    for (var i = 0; i < buttonList.length; i++) //for each different type of button
    {
        //multiply the total by the coefficients read from the buttons
        totalprice *= readbuttons(buttonList[i], yes_no_list)
    }

    var divobj = document.getElementById('totalPrice'); //grab the totalPrice element
    divobj.style.display='block'; //display the element
    divobj.innerHTML = "Total Price For the Cake $" + totalprice; // set the text for the element
}

