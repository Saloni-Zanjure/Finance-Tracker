from django.test import TestCase

from django.contrib.auth.models import User
from .models import Expense

# class ExpenseTestCase(TestCase):
#     def setUp(self):
#         """Create a user for the expense tests"""
#         self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password123')

#     def test_create_expense(self):
#         """Test that an expense can be created successfully"""
#         # Log in the user
#         self.client.login(username='testuser', password='password123')

#         # Create an expense via POST request
#         data = {
#             'amount': 100,
#             'category': 'Food',
#             'description': 'Lunch at restaurant',
#             'date': '2025-03-19',
#             'owner': self.user.id
#         }
#         response = self.client.post('/expense/create/', data)  # Adjust the URL path based on your app's urls.py

#         # Check that the expense is created
#         expense = Expense.objects.get(amount=100)
#         self.assertEqual(expense.category, 'Food')
#         self.assertEqual(expense.description, 'Lunch at restaurant')

#         # Check for a successful redirect (adjust the redirect URL after creation)
#         self.assertRedirects(response, '/expenses/')  # Adjust to the URL where users should be redirected

class ExpenseDeleteTestCase(TestCase):
    def setUp(self):
        """Create a user and an expense"""
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password123')
        self.expense = Expense.objects.create(amount=100, category='Food', description='Lunch', date='2025-03-19', owner=self.user)

    def test_delete_expense(self):
        """Test that an expense can be deleted"""
        # Log in the user
        self.client.login(username='testuser', password='password123')

        # Send a POST request to delete the expense
        response = self.client.post(f'/expense/{self.expense.id}/delete/')  # Adjust the URL path based on your app's urls.py

        # Check that the expense is deleted by querying the database
        with self.assertRaises(Expense.DoesNotExist):
            Expense.objects.get(id=self.expense.id)

        # Ensure the user is redirected to the expenses list page
        self.assertRedirects(response, '/expenses/')  # Adjust based on your redirect URL after deletion
