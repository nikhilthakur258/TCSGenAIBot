

Test Case 1:
@Test
public void testAddEmployeeRecord() {
	given()
		.baseUri("http://sample.employee.api/")
		.header("Content-Type", "application/json")
		.body("{\"name\":\"John Doe\",\"age\":\"30\",\"designation\":\"Software Engineer\"}")
	.when()
		.post("/addEmployee")
	.then()
		.statusCode(200);
}

Test Case 2:
@Test
public void testUpdateEmployeeRecord() {
	given()
		.baseUri("http://sample.employee.api/")
		.header("Content-Type", "application/json")
		.body("{\"name\":\"John Doe\",\"age\":\"32\",\"designation\":\"Software Engineer\"}")
	.when()
		.put("/updateEmployee/{id}")
	.then()
		.statusCode(200);
}

Test Case 3:
@Test
public void testGetEmployeeRecord() {
	given()
		.baseUri("http://sample.employee.api/")
		.header("Content-Type", "application/json")
	.when()
		.get("/getEmployee/{id}")
	.then()
		.statusCode(200);
}

Test Case 4:
@Test
public void testDeleteEmployeeRecord() {
	given()
		.baseUri("http://sample.employee.api/")
		.header("Content-Type", "application/json")
	.when()
		.delete("/deleteEmployee/{id}")
	.then()
		.statusCode(200);
}
