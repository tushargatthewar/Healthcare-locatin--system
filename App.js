import React, { useState } from "react";
import { View, StyleSheet, Text, Button, ScrollView } from "react-native";
import Dropdown from "./src/components/Dropdown";
import { PythonShell } from "python-shell";

const optionsList = [
  { label: 'back_pain', value: 1 },
  { label: 'constipation', value: 2 },
  { label: 'abdominal_pain', value: 3 },
  { label: 'diarrhoea', value: 4 },
  { label: 'mild_fever', value: 5 },
  { label: 'yellow_urine', value: 6 },
  { label: 'yellowing_of_eyes', value: 7 },
  { label: 'acute_liver_failure', value: 8 },
  { label: 'fluid_overload', value: 9 },
  { label: 'swelling_of_stomach', value: 10 },
  { label: 'swelled_lymph_nodes', value: 12 },
  { label: 'malaise', value: 13 },
  { label: 'blurred_and_distorted_vision', value: 14 },
  { label: 'phlegm', value: 15 },
  { label: 'throat_irritation', value: 16 },
  { label: 'redness_of_eyes', value: 17 },
  { label: 'sinus_pressure', value: 18 },
  { label: 'runny_nose', value: 19 },
  { label: 'congestion', value: 20 },
  { label: 'chest_pain', value: 31 },
];
const App = () => {
  const [selectedOptions, setSelectedOptions] = useState(Array(5).fill(null));

  const handleSelect = (index, option) => {
    setSelectedOptions((prev) => {
      const updatedSelectedOptions = [...prev];
      updatedSelectedOptions[index] = option;
      return updatedSelectedOptions;
    });
    console.log(`Selected option: ${option.label}`);
  };

  const handleSubmit = async () => {
    console.log('Selected options:', selectedOptions);

    // Convert selected options to a list of strings
    const selectedOptionsList = selectedOptions.map((option) => option.label);

    // Call Python script with selected options
    const options = {
      mode: "text",
      pythonOptions: ["-u"],
      scriptPath: "./python/ML_CODE.py", // Path to your Python script
      args: [JSON.stringify(selectedOptionsList)],
    };

    PythonShell.run("./python/ML_CODE.py", options, (err, results) => {
      if (err) throw err;
      console.log("results: ", results);
    });
  };

  return (
    <View style={styles.container}>
      <View style={styles.form}>
        <ScrollView>
          {Array(5)
            .fill(null)
            .map((_, i) => (
              <Dropdown
                key={i}
                options={optionsList}
                title={selectedOptions[i] ? selectedOptions[i].label : 'Select an option'}
                onSelect={(option) => handleSelect(i, option)}
              />
            ))}
        </ScrollView>
      </View>
      <Button title="Submit" onPress={handleSubmit} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
  },
  form: {
    marginVertical: 20,
  },
});

export default App;