<?php include 'included/header.php'; ?>
		<div class="row">
			<h1 class="page-header">
				Find Out What Your Device is Worth!
			</h1>
		</div>
		<form action="calculate.php" id="form" method="GET" onsubmit="return true;">
			<div class="cont_order">
			    <fieldset>
					<legend>Select your phone!</legend>
					<br/>

					<label>Select your phone</label>
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

					<label>Select your carrier</label>
					<select id="carrier" name='carrier' onchange="calculateTotal()">
						<option value="None">Select Carrier</option>
						<option value="AT&amp;T">AT&amp;T</option>
						<option value="Sprint">Sprint</option>
						<option value="T-Mobile">T-Mobile</option>
						<option value="Verizon">Verizon</option>
						<option value="Unbranded/Other">Unbranded/Other</option>
				    </select>

					<br/>
					<br/>

					<label>What is the condition of your phone's frame</label>
					<br/>
					<label class='radiolabel'><input type="radio"  name="frame" value="severely damaged" onclick="calculateTotal()">cracked</label><br/>
					<label class='radiolabel'><input type="radio"  name="frame" value="slightly damaged" onclick="calculateTotal()">scratched</label><br/>
					<label class='radiolabel'><input type="radio"  name="frame" value="flawless" onclick="calculateTotal()">flawless</label><br/>

					<br/>

					<label>Do you have your phone's original box?</label>
					<br>
					<label class='radiolabel'><input type="radio"  name="box" value="yes" onclick="calculateTotal()">yes</label><br/>
					<label class='radiolabel'><input type="radio"  name="box" value="no" onclick="calculateTotal()">no</label><br/>

					<br/>

					<label>How many years old is your phone?</label>
					<input type="text" id="age" name="age" onclick="calculateTotal()" /><br/>

					<div id="totalPrice" style="display: none;"></div>
				</fieldset>
			    <input type='submit' id='submit' value='Submit' onclick="calculateTotal()">
			</div> / 
		</form>
	<script type="text/javascript" src="js/formcalculations.js"></script>
	<?php echo "Your phone is worth $360.00"; ?>
	<?php echo "print technique 1:<br> ", $_GET['phone'] . ' ' .  $_GET['carrier'], "<br><br>"; ?>
	<?php echo foreach($_GET as $key => $value) { echo $key . ': ' . $value . "<br>"; } ?>
<?php include 'included/footer.php'; ?>
