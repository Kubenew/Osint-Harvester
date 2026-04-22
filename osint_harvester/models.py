from dataclasses import dataclass, field
from typing import Dict, Any, List


@dataclass
class OSINTReport:
    target: str
    target_type: str
    data: Dict[str, Any] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "target": self.target,
            "target_type": self.target_type,
            "data": self.data,
            "errors": self.errors,
        }


def to_stix_like(report: "OSINTReport") -> Dict[str, Any]:
    return {
        "type": "bundle",
        "id": f"bundle--{report.target_type}--{report.target}",
        "objects": [
            {
                "type": "indicator",
                "name": f"{report.target_type}:{report.target}",
                "pattern_type": "stix",
                "pattern": f"[{report.target_type}:value = '{report.target}']",
                "x_osint_data": report.data,
                "x_osint_errors": report.errors,
            }
        ],
    }
