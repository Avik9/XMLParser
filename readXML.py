# -*- coding: utf-8 -*-

"""
Created on Tue July 8 15:31:59 2019
@author: Avik Kadakia
"""

import csv
import glob
import os
import html
import xml
from xml.etree.cElementTree import parse

if __name__ == "__main__":

    scopeid_text = name_text = subnet_mast_text = start_range_text = end_range_text = lease_duration_text = state_text\
         = type_text = nap_enabled_text = description_text = ""

    path = input("Please enter the path to read .xml files from: ")

    # Started writing in the csv file
    with open('Parsed XML.csv', mode='w') as parsed_XML:

        employee_writer = csv.writer(parsed_XML)

        # Headers for the csv file
        employee_writer.writerow(["Name", "Scope ID", "New Name", "Subnet Mask", "Start Range", "End Range",
                                  "Lease Duration", "State", "Type", "Nap Enabled", "Description",
                                  "New Description"])

        p = 0

        # For every file in the directory
        for file in glob.glob(os.path.join(path, '*.xml')):
            try:
                x = 0
                p = p + 1
                print(str(p) + ") The title of the file is:" + file.title())

                originalFileName = file

                with open(file, 'r') as opened_file:
                    with open('tempXMLfile.xml', 'w') as temp_writable_file:

                        for line in opened_file:
                            x = x + 1
                            temp_writable_file.write(html.unescape(line))

                        print("Done Parsing")
                        temp_writable_file.flush()
                        temp_writable_file.close()

                    tree = parse('tempXMLfile.XML')
                    root = tree.getroot()

                    employee_writer.writerow([file])
                    print("Started parsing ", file.title())

                    for scope in root.iter('Scope'):
                        for ScopeID in scope.iter("ScopeId"):
                            scopeid_text = ScopeID.text

                        for name in scope.iter("Name"):
                            name_text = name.text

                        for subnet_mask in scope.iter('SubnetMask'):
                            subnet_mast_text = subnet_mask.text

                        for start_range in scope.iter("StartRange"):
                            start_range_text = start_range.text

                        for end_range in scope.iter("EndRange"):
                            end_range_text = end_range.text

                        for lease_duration in scope.iter('LeaseDuration'):
                            lease_duration_text = lease_duration.text

                        for state in scope.iter('State'):
                            state_text = state.text

                        for ScopeType in scope.iter('Type'):
                            type_text = ScopeType.text

                        for nap_enabled in scope.iter('NapEnable'):
                            nap_enabled_text = nap_enabled.text

                        for description in scope.iter('Description'):
                            if description.text is None:
                                description_text = ""

                            else:
                                description_text = description.text

                        employee_writer.writerow(
                            [name_text, scopeid_text, "", subnet_mast_text, start_range_text, end_range_text,
                             lease_duration_text, state_text, type_text, nap_enabled_text,
                             description_text, ""])

                        parsed_XML.flush()

                    print("Finished parsing ", file.title())

                parsed_XML.flush()

                os.remove('tempXMLfile.XML')
                print("File Removed!")

                print("\n")

            except xml.etree.ElementTree.ParseError as err:
                print("Found an error: ", err)

                file = 'tempXMLfile.XML'

                with open(file, 'r') as opened_error_file:

                    employee_writer.writerow([originalFileName])

                    x = y = 0
                    shouldParse = 0
                    shouldPrint = 0

                    for line in opened_error_file:

                        if "SuperScopeName" in line:
                            shouldParse = False

                        elif "<Scope>" in line:
                            shouldParse = True

                        x = x + 1

                        if shouldParse:
                            variables = [scopeid_text, name_text, subnet_mast_text, start_range_text, end_range_text,
                                         lease_duration_text, state_text, type_text, nap_enabled_text, description_text]

                            shouldPrint = 0

                            if "<ScopeId>" in line:
                                scopeid_text = line

                                scopeid_text = scopeid_text.replace(" ", "")

                                scopeid_text = scopeid_text[scopeid_text.index(">") + 1:
                                                            scopeid_text.index("<", scopeid_text.index(">"))]

                            if "<Name>" in line:
                                name_text = line

                                name_text = name_text.replace(" ", "")

                                name_text = name_text[
                                               name_text.index(">") + 1:name_text.index("<", name_text.index(">"))]

                            if "<SubnetMask>" in line:
                                subnet_mast_text = line

                                subnet_mast_text = subnet_mast_text.replace(" ", "")

                                subnet_mast_text = subnet_mast_text[
                                                   subnet_mast_text.index(">") + 1:
                                                   subnet_mast_text.index("<", subnet_mast_text.index(">"))]

                            if "<StartRange>" in line:
                                start_range_text = line

                                start_range_text = start_range_text.replace(" ", "")

                                start_range_text = start_range_text[
                                                   start_range_text.index(">") + 1:
                                                   start_range_text.index("<", start_range_text.index(">"))]

                            if "<EndRange>" in line:
                                end_range_text = line

                                end_range_text = end_range_text.replace(" ", "")

                                end_range_text = end_range_text[
                                                   end_range_text.index(">") + 1:
                                                   end_range_text.index("<", end_range_text.index(">"))]

                            if "<LeaseDuration>" in line:
                                lease_duration_text = line

                                lease_duration_text = lease_duration_text.replace(" ", "")

                                lease_duration_text = lease_duration_text[
                                                 lease_duration_text.index(">") + 1:
                                                 lease_duration_text.index("<", lease_duration_text.index(">"))]

                            if "<State>" in line:
                                state_text = line

                                state_text = state_text.replace(" ", "")

                                state_text = state_text[state_text.index(">") + 1:
                                                        state_text.index("<", state_text.index(">"))]

                            if "<Type>" in line:
                                type_text = line

                                type_text = type_text.replace(" ", "")

                                type_text = type_text[type_text.index(">") + 1:
                                                      type_text.index("<", type_text.index(">"))]

                            if "<NapEnable>" in line:
                                nap_enabled_text = line

                                nap_enabled_text = nap_enabled_text.replace(" ", "")

                                nap_enabled_text = nap_enabled_text[
                                                   nap_enabled_text.index(">") + 1:
                                                   nap_enabled_text.index("<", nap_enabled_text.index(">"))]

                            if "<Description>" in line:

                                shouldPrint = 1

                                description_text = line

                                description_text = description_text.replace(" ", "")

                                description_text = description_text[description_text.index(">") + 1:
                                                                    description_text.index("<",
                                                                                           description_text.index(">"))]

                            if "<Description />" in line:
                                shouldPrint = 1
                                description_text = ""

                        if shouldParse and shouldPrint:
                            employee_writer.writerow(
                                [scopeid_text, name_text, "", subnet_mast_text, start_range_text, end_range_text,
                                 lease_duration_text, state_text, type_text, nap_enabled_text,
                                 description_text, ""])

                        else:
                            pass

                        parsed_XML.flush()

    parsed_XML.close()
