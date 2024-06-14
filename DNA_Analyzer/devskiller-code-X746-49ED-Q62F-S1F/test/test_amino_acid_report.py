import unittest

from app.dna_analyser import DNAAnalyser


class TestReport(unittest.TestCase):
    """Amino Acid Strands Report testing class"""

    def test_codon_mapping(self):
        """Test codon mapping"""
        result = self._sut.get_amino_acids_report("AAACCCAATTTTTTACACAGCTGCTGGGCCCAGT")
        assert result.get("Proline") == 1

    def test_codon_mapping_wrong_result(self):
        """Test codon mapping with wrong result"""
        result = self._sut.get_amino_acids_report("AAACCCAATTTTTT")
        assert "Opal" not in result

    def test_codon_mapping_new_values(self):
        """Test codon mapping with new values"""
        result = self._sut.get_amino_acids_report(
            "CTAGATCGTATCGGTTACTGTGGGGAAACCTGCATGCATGCATG"
        )
        assert result.get("Alanine") == 1
        assert result.get("Glycine") == 2

    def test_amino_length(self):
        """Test report length"""
        result = self._sut.get_amino_acids_report(
            "CTAGATCGTATCGGTTACTGTGGGGAAACCTGCATGCATGCATG"
        )

        assert len(result.keys()) == 12

    def test_total_count(self):
        """Test report count"""
        result = self._sut.get_amino_acids_report("CTAGATC")

        assert sum(result.values()) == 2

    def setUp(self):
        self._sut = DNAAnalyser()
