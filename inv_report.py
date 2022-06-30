                   
                   def write_inv_report(inv_list, match):
                    for i in range(1, row_num+1):
                        for key in match:
                        
                            #print('key = ', key)
                            inv_list = match.get(key)
                            item = pickList.iat[i-1, purch_item_index]
                            l=1
                            #print('item = ', item)
                            #print('length of inv_list = ', len(inv_list))

                            if item == key:
                                if  len(inv_list) == 1:
                                    #print('item match = ', match)
                                    purch_item_row_idx = pickList[pickList['Item'] == key].index[0]
                                    purch_item = pickList.loc[purch_item_row_idx, 'Item']
                                    purch_desc = pickList.loc[purch_item_row_idx, 'Description']
                                    purch_qty = pickList.loc[purch_item_row_idx, 'Project Quantity']

                                    
                                    try:
                                        InvReport.write(r+2, 0, purch_item, outer_border_all_format)
                                        InvReport.write(r+2, 1, purch_desc, outer_border_all_format)
                                        InvReport.write(r+2, 2, purch_qty, outer_border_all_format)
                                    except:
                                        InvReport.write(r+2, 0, "", outer_border_all_format)
                                        InvReport.write(r+2, 1, "", outer_border_all_format)
                                        InvReport.write(r+2, 2, "", outer_border_all_format)
                                    
                                   

                                    for i in range(0, len(inv_list)):
                                        #print('item matches: ', purch_item)

                                        inv_mfg = current_inventory['Mfg.'].values[inv_list[i]]
                                        inv_model = current_inventory['Mfg. Part #'].values[inv_list[i]]
                                        inv_desc = current_inventory['Description'].values[inv_list[i]]
                                        inv_qty = current_inventory['Qty'].values[inv_list[i]]
                                        inv_location = current_inventory['Location'].values[inv_list[i]]
                                        inv_tag = current_inventory['Tag #'].values[inv_list[i]]

                                        #InvReport.write(i+3, 0, '', outer_last_border_format)
                                        #InvReport.write(i+3, 1, '', outer_last_border_format)
                                        #InvReport.write(i+3, 2, '', outer_last_border_format)
                                        try:
                                            InvReport.write(r+2, 4, inv_mfg, outer_last_border_format)
                                            InvReport.write(r+2, 5, inv_model, outer_last_border_format)
                                            InvReport.write(r+2, 6, inv_desc, outer_last_border_format)
                                            InvReport.write(r+2, 7, inv_qty, outer_last_border_format)
                                            InvReport.write(r+2, 8, inv_location, outer_last_border_format)
                                            InvReport.write(r+2, 9, inv_tag, outer_last_border_format)
                                        except:
                                            InvReport.write(r+2, 4, "", outer_last_border_format)
                                            InvReport.write(r+2, 5, "", outer_last_border_format)
                                            InvReport.write(r+2, 6, "", outer_last_border_format)
                                            InvReport.write(r+2, 7, "", outer_last_border_format)
                                            InvReport.write(r+2, 8, "", outer_last_border_format)
                                            InvReport.write(r+2, 9, "", outer_last_border_format)

                                        r= r+1


                                if  len(inv_list) > 1:
                                    if l == 1:
                                        i=0
                                        #print('item match = ', match)
                                        print('l == 0')
                                        purch_item_row_idx = pickList[pickList['Item'] == key].index[0]
                                        purch_item = pickList.loc[purch_item_row_idx, 'Item']
                                        purch_desc = pickList.loc[purch_item_row_idx, 'Description']
                                        purch_qty = pickList.loc[purch_item_row_idx, 'Project Quantity']

                                        inv_mfg = current_inventory['Mfg.'].values[inv_list[i]]
                                        inv_model = current_inventory['Mfg. Part #'].values[inv_list[i]]
                                        inv_desc = current_inventory['Description'].values[inv_list[i]]
                                        inv_qty = current_inventory['Qty'].values[inv_list[i]]
                                        inv_location = current_inventory['Location'].values[inv_list[i]]
                                        inv_tag = current_inventory['Tag #'].values[inv_list[i]]

                                        try:
                                            InvReport.write(r+2, 0, purch_item, outer_border_format)
                                            InvReport.write(r+2, 1, purch_desc, outer_border_format)
                                            InvReport.write(r+2, 2, purch_qty, outer_border_format) 

                                            InvReport.write(r+2, 4, inv_mfg, outer_last_border_format)
                                            InvReport.write(r+2, 5, inv_model, outer_last_border_format)
                                            InvReport.write(r+2, 6, inv_desc, outer_last_border_format)
                                            InvReport.write(r+2, 7, inv_qty, outer_last_border_format)
                                            InvReport.write(r+2, 8, inv_location, outer_last_border_format)
                                            InvReport.write(r+2, 9, inv_tag, outer_last_border_format)

                                        except:
                                            InvReport.write(r+2, 0, "", outer_border_format)
                                            InvReport.write(r+2, 1, "", outer_border_format)
                                            InvReport.write(r+2, 2, "", outer_border_format) 

                                            InvReport.write(r+2, 4, "", outer_last_border_format)
                                            InvReport.write(r+2, 5, "", outer_last_border_format)
                                            InvReport.write(r+2, 6, "", outer_last_border_format)
                                            InvReport.write(r+2, 7, "", outer_last_border_format)
                                            InvReport.write(r+2, 8, "", outer_last_border_format)
                                            InvReport.write(r+2, 9, "", outer_last_border_format)


                                        r = r+1                          
                                    
                                    for i in range(1, len(inv_list)):
                                        #print('item matches: ', purch_item)
                                        l = l+1
                                        print('l = ', l)
                                        print('len(inv_list) = ', len(inv_list))

                                        if l <= (len(inv_list)):
                                            if l == len(inv_list):
                                                print('l == len(inv_list)')
                                                inv_mfg = current_inventory['Mfg.'].values[inv_list[i]]
                                                inv_model = current_inventory['Mfg. Part #'].values[inv_list[i]]
                                                inv_desc = current_inventory['Description'].values[inv_list[i]]
                                                inv_qty = current_inventory['Qty'].values[inv_list[i]]
                                                inv_location = current_inventory['Location'].values[inv_list[i]]
                                                inv_tag = current_inventory['Tag #'].values[inv_list[i]]

                                                InvReport.write(r+2, 0, "", outer_last_border_format)
                                                InvReport.write(r+2, 1, "", outer_last_border_format)
                                                InvReport.write(r+2, 2, "", outer_last_border_format)
                                                
                                                try:
                                                    InvReport.write(r+2, 4, inv_mfg, outer_last_border_format)
                                                    InvReport.write(r+2, 5, inv_model, outer_last_border_format)
                                                    InvReport.write(r+2, 6, inv_desc, outer_last_border_format)
                                                    InvReport.write(r+2, 7, inv_qty, outer_last_border_format)
                                                    InvReport.write(r+2, 8, inv_location, outer_last_border_format)
                                                    InvReport.write(r+2, 9, inv_tag, outer_last_border_format)
                                                except:
                                                    InvReport.write(r+2, 4, "", outer_last_border_format)
                                                    InvReport.write(r+2, 5, "", outer_last_border_format)
                                                    InvReport.write(r+2, 6, "", outer_last_border_format)
                                                    InvReport.write(r+2, 7, "", outer_last_border_format)
                                                    InvReport.write(r+2, 8, "", outer_last_border_format)
                                                    InvReport.write(r+2, 9, "", outer_last_border_format)
                                            
                                                r = r+1
                                            if l < len(inv_list):
                                                print('l < len(inv_list)')
                                                inv_mfg = current_inventory['Mfg.'].values[inv_list[i]]
                                                inv_model = current_inventory['Mfg. Part #'].values[inv_list[i]]
                                                inv_desc = current_inventory['Description'].values[inv_list[i]]
                                                inv_qty = current_inventory['Qty'].values[inv_list[i]]
                                                inv_location = current_inventory['Location'].values[inv_list[i]]
                                                inv_tag = current_inventory['Tag #'].values[inv_list[i]]

                                                InvReport.write(r+2, 0, "", outer_border_format)
                                                InvReport.write(r+2, 1, "", outer_border_format)
                                                InvReport.write(r+2, 2, "", outer_border_format)
                                                
                                                try:
                                                    InvReport.write(r+2, 4, inv_mfg, outer_last_border_format)
                                                    InvReport.write(r+2, 5, inv_model, outer_last_border_format)
                                                    InvReport.write(r+2, 6, inv_desc, outer_last_border_format)
                                                    InvReport.write(r+2, 7, inv_qty, outer_last_border_format)
                                                    InvReport.write(r+2, 8, inv_location, outer_last_border_format)
                                                    InvReport.write(r+2, 9, inv_tag, outer_last_border_format)
                                                except:
                                                    InvReport.write(r+2, 4, "", outer_last_border_format)
                                                    InvReport.write(r+2, 5, "", outer_last_border_format)
                                                    InvReport.write(r+2, 6, "", outer_last_border_format)
                                                    InvReport.write(r+2, 7, "", outer_last_border_format)
                                                    InvReport.write(r+2, 8, "", outer_last_border_format)
                                                    InvReport.write(r+2, 9, "", outer_last_border_format)

                                                r = r+1

                                        else:
                                            pass
                                    else:
                                        pass            
                                else:
                                    pass
                            else:
                                pass