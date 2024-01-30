# from admin_tools.dashboard import Dashboard, AppIndexDashboard
#
# class CustomIndexDashboard(Dashboard):
#     def init_with_context(self, context):
#         self.children.append(AppIndexDashboard(
#             name ='Products',
#             app_label ='fashion_spot',
#         ))
#
#         self.children.append(AppIndexDashboard(
#             name='Users',
#             app_label='auth',
#         ))
#
#         self.children.append(AppIndexDashboard(
#             name='Orders',
#             app_label='fashion_spot'
#         ))