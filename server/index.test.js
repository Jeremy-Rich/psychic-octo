test('Should return a 200 status code when accessing the root route', async () => {
    const response = await request(app).get('/');
    expect(response.statusCode).toBe(200);
    expect(response.text).toBe('Server is running');  // New assertion
  });