<?php include 'included/header.php'; ?>
	<div class="container">
		<div class="row">
			<h1 class="page-header">
				Find Out What Your Device is Worth!
			</h1>
		</div>
		<form action="" id="form" onsubmit="return false;">
			    <div class="cont_order">
			       <fieldset>
				<legend>Select your phone!</legend>
				<label >Select your phone manufacturer</label>
				<br>
				<label class='radiolabel'><input type="radio"  name="manufacturer" value="Samsung" onclick="calculateTotal()" />Samsung</label><br/>
				<label class='radiolabel'><input type="radio"  name="manufacturer" value="LG" onclick="calculateTotal()" />LG</label><br/>
				<label class='radiolabel'><input type="radio"  name="manufacturer" value="HTC" onclick="calculateTotal()" />HTC</label><br/>
				<label class='radiolabel'><input type="radio"  name="manufacturer" value="Apple" onclick="calculateTotal()" />Apple</label><br/>

				<br/>

				<label >Select your phone</label>
				<select id="phone" name='phone' onchange="calculateTotal()">
				<option value="None">Select Phone</option>
				<option value="None">Samsung Galaxy</option>
				<option value="Samsung Galaxy S6 Edge">....Samsung Galaxy S6 Edge</option>
				<option value="Samsung Galaxy S6">....Samsung Galaxy S6</option>
				<option value="Samsung Galaxy S5">....Samsung Galaxy S5</option>
				<option value="Samsung Galaxy S4">....Samsung Galaxy S4</option>
				<option value="Samsung Galaxy S3">....Samsung Galaxy S3</option>
				<option value="Samsung Galaxy Note 5">....Samsung Galaxy Note 5</option>
				<option value="Samsung Galaxy Note 4">....Samsung Galaxy Note 4</option>
				<option value="Samsung Galaxy Note 3">....Samsung Galaxy Note 3</option>
				<option value="Samsung Galaxy Note 2">....Samsung Galaxy Note 2</option>
				<option value="None">LG</option>
				<option value="LG G4">....LG G4</option>
				<option value="LG G3">....LG G3</option>
				<option value="LG G2">....LG G2</option>
				<option value="None">HTC</option>
				<option value="HTC One M8">....HTC One M8</option>
				<option value="HTC One M7">....HTC One M7</option>
				<option value="None">Apple</option>
				<option value="Apple iPhone 6s">....Apple iPhone 6s</option>
				<option value="Apple iPhone 6 Plus">....Apple iPhone 6 Plus</option>
				<option value="Apple iPhone 6">....Apple iPhone 6</option>
				<option value="Apple iPhone 5s">....Apple iPhone 5s</option>
				<option value="Apple iPhone 5c">....Apple iPhone 5c</option>
				<option value="Apple iPhone 5">....Apple iPhone 5</option>
				<option value="Apple iPhone 4s">....Apple iPhone 4s</option>
				<option value="Apple iPhone 4">....Apple iPhone 4</option>
			       </select>

				<br/>
				<br/>

				<label >Select your carrier</label>
				<select id="carrier" name='carrier' onchange="calculateTotal()">
				<option value="None">Select Carrier</option>
				<option value="AT&T">AT&T</option>
				<option value="Sprint">Sprint</option>
				<option value="T-Mobile">T-Mobile</option>
				<option value="Verizon">Verizon</option>
				<option value="Cricket">Cricket</option>
				<option value="Virgin Mobile">Virgin Mobile</option>
				<option value="Unbranded/Other">Unbranded/Other</option>
			       </select>

				<br/>
				<br/>

				<label >Is your phone under contract?</label>
				<br>
				<label class='radiolabel'><input type="radio"  name="contract" value="yes" onclick="calculateTotal()" />yes</label><br/>
				<label class='radiolabel'><input type="radio"  name="contract" value="no" onclick="calculateTotal()" />no</label><br/>

				<br/>

				<label >Is your phone used?</label>
				<br>
				<label class='radiolabel'><input type="radio"  name="used" value="yes" onclick="calculateTotal()" />yes</label><br/>
				<label class='radiolabel'><input type="radio"  name="used" value="no" onclick="calculateTotal()" />no</label><br/>

				<br/>

				<label >Is your phone covered by insurance?</label>
				<br>
				<label class='radiolabel'><input type="radio"  name="insurance" value="yes" onclick="calculateTotal()" />yes</label><br/>
				<label class='radiolabel'><input type="radio"  name="insurance" value="no" onclick="calculateTotal()" />no</label><br/>

				<br/>

				<label >Does your phone power on?</label>
				<br>
				<label class='radiolabel'><input type="radio"  name="power" value="yes" onclick="calculateTotal()" />yes</label><br/>
				<label class='radiolabel'><input type="radio"  name="power" value="no" onclick="calculateTotal()" />no</label><br/>

				<br/>

				<label >Does your phone have water damage?</label>
				<br>
				<label class='radiolabel'><input type="radio"  name="water" value="yes" onclick="calculateTotal()" />yes</label><br/>
				<label class='radiolabel'><input type="radio"  name="water" value="no" onclick="calculateTotal()" />no</label><br/>

				<br/>

				<label >What is the condition of your screen?</label>
				<br>
				<label class='radiolabel'><input type="radio"  name="cracked" value="cracked" onclick="calculateTotal()" />cracked</label><br/>
				<label class='radiolabel'><input type="radio"  name="scratched" value="scratched" onclick="calculateTotal()" />scratched</label><br/>
				<label class='radiolabel'><input type="radio"  name="flawless" value="flawless" onclick="calculateTotal()" />flawless</label><br/>

				<br/>

				<label >How many broken buttons does your phone have?</label>
				<br>
				<input type="text" id="buttons" name="buttons" onclick="calculateTotal()" /><br/>

				<br/>

				<label >What is the condition of your phone's frame</label>
				<br>
				<label class='radiolabel'><input type="radio"  name="cracked" value="severely damaged" onclick="calculateTotal()" />cracked</label><br/>
				<label class='radiolabel'><input type="radio"  name="scratched" value="slightly damaged" onclick="calculateTotal()" />scratched</label><br/>
				<label class='radiolabel'><input type="radio"  name="flawless" value="flawless" onclick="calculateTotal()" />flawless</label><br/>

				<br/>

				<label >Do you have your phone's original box?</label>
				<br>
				<label class='radiolabel'><input type="radio"  name="box" value="yes" onclick="calculateTotal()" />yes</label><br/>
				<label class='radiolabel'><input type="radio"  name="box" value="no" onclick="calculateTotal()" />no</label><br/>

				<br/>

				<label >How many years old is your phone?</label>
				<input type="text" id="buttons" name="buttons" onclick="calculateTotal()" /><br/>

				<div id="totalPrice" style="display: none;"></div>
				
				</fieldset>
			    </div>
			    
				<div class="cont_details">
				<fieldset>
				<legend>Contact Details</legend>
				<label for='name'>Name</label>
				<input type="text" id="name" name='name' />
				<br/>
				<label for='email'>Email Address</label>
				<input type="text" id="address" name='address' />
				<br/>
				</fieldset>
			    </div>
			    <input type='submit' id='submit' value='Submit' onclick="calculateTotal()" />
			</div>  
		</form>
	</div>
	<script type="text/javascript" src="js/formcalculations.js"></script>
<?php include 'included/footer.php'; ?>
