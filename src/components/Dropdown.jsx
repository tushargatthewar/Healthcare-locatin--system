import React, { useState } from "react";
import { View, StyleSheet, Text, TouchableOpacity, ScrollView } from "react-native";

const Dropdown = ({ options, title, onSelect }) => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleDropdown = () => {
    setIsOpen(!isOpen);
  };

  const handleSelect = (option) => {
    onSelect(option);
    setIsOpen(false);
  };

  return (
    <View style={styles.container}>
      <TouchableOpacity onPress={toggleDropdown}>
        <View style={styles.dropdownTitle}>
          <Text style={styles.title}>{title}</Text>
          <Text style={styles.selectedOption}>{onSelect ? onSelect.label : 'Select an option'}</Text>
        </View>
      </TouchableOpacity>
      {isOpen && (
        <View style={styles.options}>
          <ScrollView>
            {options.map((option) => (
              <TouchableOpacity
                key={option.value}
                onPress={() => handleSelect(option)}
                style={styles.option}
              >
                <Text style={styles.optionText}>{option.label}</Text>
              </TouchableOpacity>
            ))}
          </ScrollView>
        </View>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    width: '100%',
    marginVertical: 10,
  },
  dropdownTitle: {
    padding: 10,
    backgroundColor: '#fff',
    borderColor: '#ccc',
    borderWidth: 1,
    borderRadius: 5,
    display: 'flex',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
  },
  title: {
    fontSize: 16,
    fontWeight: 'bold',
  },
  selectedOption: {
    fontSize: 16,
    marginLeft: 10,
  },
  options: {
    width: '100%',
    borderColor: '#ccc',
    borderWidth: 1,
    borderRadius: 5,
    marginTop: 10,
  },
  option: {
    padding: 10,
    borderBottomWidth: 1,
    borderBottomColor: '#ccc',
  },
  optionText: {
    fontSize: 16,
  },
});

export default Dropdown;