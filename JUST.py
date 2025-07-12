# from bs4 import BeautifulSoup
# import pandas as pd
#
# # HTML content (replace with actual file reading if needed)
# html_content = """
# <tr>
#                                 <td align="center" bgcolor="#f2f0f0" class="sell_catagory">차량정보</td>
#                                 <td width="96" align="center" bgcolor="#f2f0f0" class="sell_catagory">작성자</td>
#                                 <td width="87" align="center" bgcolor="#f2f0f0" class="sell_catagory">가격</td>
#                                 <td width="64" align="center" bgcolor="#f2f0f0" class="sell_catagory">게시일</td>
#                               </tr>
#                               <tr>
#                                 <td bgcolor="#ffffff">
#                                   <table width="100%" border="0" cellspacing="0" cellpadding="5">
#                                     <tbody>
#                                       <tr>
#                                         <td width="267">
#                                           <div
#                                             style="width:267px;height:150px;z-index=1;overflow:hidden;border:1px #e1e1e1 solid;">
#                                             <a href="/mainpage/business/cars/cars_read.asp?id=busi2&amp;idx=233463"><img
#                                                 src="/fileServer/ImageServer/thum/busi2/20257/2025070815293289291.jpg"
#                                                 width="267"
#                                                 onerror="this.src='/mainpage/business/img/nophoto2.jpg'"></a></div>
#                                         </td>
#                                         <td style="padding-left:20px;" valign="top">
#                                           <div style="margin-top:10px;"><span class="sell_catagory"
#                                               style="margin-left:10px;">[Fullerton / CA]</span></div>
#                                           <div class="sell_title" style="word-break:break-all"><a
#                                               href="/mainpage/business/cars/cars_read.asp?id=busi2&amp;idx=233463">7월
#                                               특별한 세일 놓치지마세요 ◈ 초특가 리스 ◈ 스페셜!</a></div>
#                                           <div style="margin-top:15px;" class="dealerlist">1Miles / 2025년식</div>
#                                         </td>
#                                       </tr>
#                                     </tbody>
#                                   </table>
#                                 </td>
#                                 <td bgcolor="#ffffff" align="center">
#                                   <div class="sell_catagory">danny park<br>
#                                     <font color="#2424e8">직거래</font>
#                                   </div>
#                                 </td>
#                                 <td bgcolor="#ffffff" align="right" class="price">$50</td>
#                                 <td bgcolor="#ffffff" align="center" class="note_date" style="letter-spacing:-1px;">
#                                   2025-07-08</td>
#                               </tr>
#                               <tr>
#                                 <td bgcolor="#ffffff">
#                                   <table width="100%" border="0" cellspacing="0" cellpadding="5">
#                                     <tbody>
#                                       <tr>
#                                         <td width="267">
#                                           <div
#                                             style="width:267px;height:150px;z-index=1;overflow:hidden;border:1px #e1e1e1 solid;">
#                                             <a href="/mainpage/business/cars/cars_read.asp?id=busi2&amp;idx=231775"><img
#                                                 src="/fileServer/ImageServer/thum/busi2/20257/2025070716220327011.jpg"
#                                                 width="267"
#                                                 onerror="this.src='/mainpage/business/img/nophoto2.jpg'"></a></div>
#                                         </td>
#                                         <td style="padding-left:20px;" valign="top">
#                                           <div style="margin-top:10px;"><span class="sell_catagory"
#                                               style="margin-left:10px;">[Fullerton / CA]</span></div>
#                                           <div class="sell_title" style="word-break:break-all"><a
#                                               href="/mainpage/business/cars/cars_read.asp?id=busi2&amp;idx=231775">7월
#                                               손님이 원하는가격! ◈ 저렴한 리스 ◈ 스페셜/리스리턴/중고차량 최고가격 매입/시간상관없이 연락주세요 562-760-6295
#                                               대니입니다!</a></div>
#                                           <div style="margin-top:15px;" class="dealerlist">1Miles / 2025년식</div>
#                                         </td>
#                                       </tr>
#                                     </tbody>
#                                   </table>
#                                 </td>
#                                 <td bgcolor="#ffffff" align="center">
#                                   <div class="sell_catagory">danny park<br>
#                                     <font color="#2424e8">직거래</font>
#                                   </div>
#                                 </td>
#                                 <td bgcolor="#ffffff" align="right" class="price">$50</td>
#                                 <td bgcolor="#ffffff" align="center" class="note_date" style="letter-spacing:-1px;">
#                                   2025-07-07</td>
#                               </tr>
#                               <tr>
#                                 <td bgcolor="#ffffff">
#                                   <table width="100%" border="0" cellspacing="0" cellpadding="5">
#                                     <tbody>
#                                       <tr>
#                                         <td width="267">
#                                           <div
#                                             style="width:267px;height:150px;z-index=1;overflow:hidden;border:1px #e1e1e1 solid;">
#                                             <a href="/mainpage/business/cars/cars_read.asp?id=busi2&amp;idx=231106"><img
#                                                 src="/fileServer/ImageServer/thum/busi2/20257/2025070613510030461.jpg"
#                                                 width="267"
#                                                 onerror="this.src='/mainpage/business/img/nophoto2.jpg'"></a></div>
#                                         </td>
#                                         <td style="padding-left:20px;" valign="top">
#                                           <div style="margin-top:10px;"><span class="sell_catagory"
#                                               style="margin-left:10px;">[Fullerton / CA]</span></div>
#                                           <div class="sell_title" style="word-break:break-all"><a
#                                               href="/mainpage/business/cars/cars_read.asp?id=busi2&amp;idx=231106">7월
#                                               새차/리스 최저리스 ◈중고차 매입 전문◈</a></div>
#                                           <div style="margin-top:15px;" class="dealerlist">1Miles / 2025년식</div>
#                                         </td>
#                                       </tr>
#                                     </tbody>
#                                   </table>
#                                 </td>
#                                 <td bgcolor="#ffffff" align="center">
#                                   <div class="sell_catagory">danny park<br>
#                                     <font color="#2424e8">직거래</font>
#                                   </div>
#                                 </td>
#                                 <td bgcolor="#ffffff" align="right" class="price">$50</td>
#                                 <td bgcolor="#ffffff" align="center" class="note_date" style="letter-spacing:-1px;">
#                                   2025-07-06</td>
#                               </tr>
# <!-- Add more rows or load from file -->
# """
#
# # Parse HTML with BeautifulSoup
# soup = BeautifulSoup(html_content, 'html.parser')
#
# # Initialize lists to store data
# data = {
#     'Title': [],
#     'Location': [],
#     'Mileage': [],
#     'Year': [],
#     'Author': [],
#     'Price': [],
#     'Date': []
# }
#
# # Find all rows except the header
# rows = soup.find_all('tr')[1:]  # Skip the header row
#
# for index, row in enumerate(rows):
#     try:
#         # Extract vehicle info
#         vehicle_info_td = row.find('td', bgcolor="#ffffff")
#         if not vehicle_info_td:
#             print(f"Warning: No <td bgcolor='#ffffff'> found in row {index + 1}")
#             continue
#
#         vehicle_info = vehicle_info_td.find('table')
#         if not vehicle_info:
#             print(f"Warning: No <table> found in row {index + 1}")
#             continue
#
#         location = vehicle_info.find('span', class_='sell_catagory')
#         location = location.text.strip() if location else 'N/A'
#
#         title = vehicle_info.find('div', class_='sell_title')
#         title = title.text.strip() if title else 'N/A'
#
#         dealer_info = vehicle_info.find('div', class_='dealerlist')
#         dealer_info = dealer_info.text.strip() if dealer_info else 'N/A / N/A'
#         mileage, year = dealer_info.split(' / ') if ' / ' in dealer_info else ('N/A', 'N/A')
#
#         # Extract author
#         author_td = row.find('td', align="center")
#         author = author_td.find('div', class_='sell_catagory').text.split('\n')[0].strip() if author_td else 'N/A'
#
#         # Extract price
#         price = row.find('td', class_='price')
#         price = price.text.strip() if price else 'N/A'
#
#         # Extract date
#         date = row.find('td', class_='note_date')
#         date = date.text.strip() if date else 'N/A'
#
#         # Append to data dictionary
#         data['Title'].append(title)
#         data['Location'].append(location)
#         data['Mileage'].append(mileage)
#         data['Year'].append(year)
#         data['Author'].append(author)
#         data['Price'].append(price)
#         data['Date'].append(date)
#
#     except Exception as e:
#         print(f"Error processing row {index + 1}: {e}")
#         continue
#
# # Create DataFrame
# df = pd.DataFrame(data)
#
# # Save to Excel
# df.to_excel('car_listings.xlsx', index=False)
#
# print(f"Data has been saved to 'car_listings.xlsx'. Processed {len(df)} rows.")
#
#
# async def delete_listing_by_idx(self, page: Page, idx: str):
#     """Delete a listing by its idx, handling JS alerts with custom timing and robust selector"""
#     try:
#         import asyncio
#         self.logger.info(f"Navigating to listings page to delete idx={idx}")
#         await page.goto("https://www.musalist.com:442/mainpage/business/member/mylist.asp")
#         await page.wait_for_load_state('networkidle')
#         await asyncio.sleep(2)  # Wait 2 seconds after navigation
#         # Use robust CSS selector for the delete button
#         delete_img_selector = f"img[alt='삭제'][onclick^=\"del('{idx}',\"]"
#         delete_button = await page.query_selector(delete_img_selector)
#         if delete_button:
#             self.logger.info(
#                 f"Found delete button for idx={idx}, waiting 2 seconds, then clicking and waiting for confirmation dialog...")
#             await asyncio.sleep(10)  # Wait 2 seconds before clicking delete
#             await delete_button.scroll_into_view_if_needed()
#             await delete_button.click()
#             self.logger.info(f"Clicked delete button for idx={idx}")
#             await asyncio.sleep(5000)  # Wait for the dialog to appear
#             # Handle first alert (confirmation)
#             dialog1 = await page.wait_for_event("dialog", timeout=10000)
#             self.logger.info(f"Confirmation dialog appeared: {dialog1.message}")
#             await asyncio.sleep(2)
#             await dialog1.accept()
#             # Handle second alert (success)
#             dialog2 = await page.wait_for_event("dialog", timeout=10000)
#             self.logger.info(f"Success dialog appeared: {dialog2.message}")
#             await asyncio.sleep(2)
#             await dialog2.accept()
#             self.logger.info(f"Deleted listing idx={idx} successfully.")
#         else:
#             self.logger.warning(f"Delete button not found for idx={idx} using selector: {delete_img_selector}")
#     except Exception as e:
#         self.logger.error(f"Error deleting listing idx={idx}: {e}")
